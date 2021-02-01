import json
import copy
from collections import defaultdict

import ODWN_reader


def convert(old_json):

    new_json = {"lus" : []}

    agent_methods = defaultdict(int)
    agents = defaultdict(int)
    methods = defaultdict(int)
    match_rels = defaultdict(int)

    for old_lu_info in old_json['lus']:

        new_lu_info = copy.deepcopy(old_lu_info)
        method = old_lu_info['provenance']

        del new_lu_info['optional_lu_attrs']

        agent_method = old_lu_info['optional_lu_attrs'].get('Method')
        if agent_method is None:
            continue

        # get agent and method
        if method == 'manual':
            agent = 'ThomasKlein'
        elif method == 'automatic':
            split = agent_method.split('_')
            agent = split[0]
            if len(split) == 2:
                method = split[1]
        else:
            raise Exception(f'method not known: {method}')


        new_lu_info['agent'] = agent
        new_lu_info['provenance'] = method

        # get rbn lu id and rel match
        optional_lu_attrs = old_lu_info['optional_lu_attrs']
        rbn_sense_id = optional_lu_attrs.get('RBN_LU_ID')
        assert rbn_sense_id is not None, old_lu_info
        rel_match = optional_lu_attrs.get('RBN_matching_relation')

        if rel_match == 'near_equivalence':
            skos_rel = 'closeMatch'
        elif rel_match == 'equivalence':
            skos_rel = 'exactMatch'

        assert rel_match is not None, old_lu_info

        skos_predicate_to_external_references = {
            skos_rel: [ODWN_reader.senseid_to_uri[rbn_sense_id]]
        }

        new_lu_info['skos_predicate_to_external_references'] = skos_predicate_to_external_references

        agents[agent] += 1
        agent_methods[(agent, method)] += 1
        methods[method] += 1
        match_rels[rel_match] += 1

        new_json['lus'].append(new_lu_info)

    print()
    print(f'agent and methods: {agent_methods}')
    print(f'agents: {agents}')
    print(f'methods: {methods}')
    print(f'matching rels: {match_rels}')

    return new_json


old_json_path = '../res/json/iterations_1_2.json'
new_json_path = '../res/json/iterations_1_2_v2.json'

old_json = json.load(open(old_json_path))

# convert
new_json = convert(old_json=old_json)

with open(new_json_path, 'w') as outfile:
    json.dump(new_json,
              outfile,
              indent=4,
              sort_keys=True)
