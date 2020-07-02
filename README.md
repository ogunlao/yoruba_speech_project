# Yoruba Speech Dataset for Low-resource speech modelling

This repo contains over 3 hours of recorded yoruba text from 1 native yoruba male speaker.

## Downloading

Go to your terminal and enter;

```git
git clone https://github.com/ogunlao/yoruba_speech_project.git
```

This adds a folder "yoruba_speech_project" to your local directory.

## Statistics

- 1079 recordings of a maximum of 20 word length per recording
- 3.06 total recording hours
- 22 folders each containing 49 recorded audio with their respective metadata.

Recordings are divided into folders for easy access.

## Collection

Text dataset used for recording was collected from [Niger Volta LTI](https://github.com/Niger-Volta-LTI/yoruba-text/blob/master/TheYorubaBlog/theyorubablog_dot_com.raw.txt). It had a smooth narrative which made the text interesting to read.

Recording was done using the [Lig-Aikuma](https://lig-aikuma.imag.fr/tutorial/) Android app. It is an easy-to-use app with good interface for recording and elicitation. It offers 6 modes of usage;

- Recording
- Respeaking
- Translating
- Elicitation
- Check
- Share

The elicitation mode was used in data collection where a displayed text is read carefully by the speaker during recording.

## Preprocessing

preprocessing involved;

- validating data for errors and removing corrupt files
- merging folders
- splitting data into train, val and test samples

Two main dataset directory with subdirectories;

- `recordings` contain the unprocessed recorded files and metadata
- `data/records` contain split data

Raw speech dataset split into;

- 1 hour of speech data (split into train and val)
- 1 hour of speech as test set
- Additional extra 1 hour of speech as extra data
- each contained in `data/records/train`, `data/records/val`, `data/records/extra` respectively

All preprocessing can be accessed through the notebook `yoruba_speech_preprocessing` and script `yor_processor`

Note that a python installation is required with some dependencies;

- numpy
- wave
- contextlib

## Application

The dataset can be used majorly for low-resource speech modelling. An example is to learn a global representation using some high-resource data like LibriSpeech and fine-tune on this dataset for Speech-to-text.

## Problems Encountered

- Difficult to eliminate noise from the surrounding, when recording.
- Some words in text were difficult to pronounce without proper accents.
- Recording speech takes time and can become uninteresting to perform quickly.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)