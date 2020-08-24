# Dutch FrameNet

The purpose of this repository is to facilitate the construction and distribution of Dutch FrameNet.
The only goal is to host the data publicly such that it
can be downloaded and we can make use of versioning.

## Contents
Apart from the **res** and **doc** folders, the contents of this repository are the files as needed
to load the lexicon using the NLTK package.
We refer to https://github.com/cltl/FrameNetNLTK
for instructions on how to load and edit the lexicon.

The **res** folder contains two subfolders:
* **json**: the repository https://github.com/cltl/FrameNetNLTK accomodates to add a batch of LUs with a JSON file as input. This folder can be used to store those JSON files.
* **descriptive_statistics**: the repository https://github.com/cltl/FrameNetNLTK allows for generating a html page with descriptive statistics about the lexicon. The descriptive statistics about each version can be stored in this folder.

The **doc** folder contains Markdown files, each containing information about a release.

## Usage
If you have edited the lexicon, you can update this repository in the following way:
* replace all FrameNet files in the NLTK format (mostly XML files or folders containing XML files)
* provided you used a JSON file to add a batch of LUs, you can add this to **res/json**
* please describe what has been changed in a new file in **doc**
* please add descriptive statistics about your release in **res/descriptive_statistics**.
* create a release on GitHub and update GitHub Pages

## Authors
* **Marten Postma** (m.c.postma@vu.nl)

## License
This project is licensed under the CC-BY 3.0 license - see the [LICENSE.md](LICENSE.md) file for details
