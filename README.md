# video_to_sub_and_emotion
This module takes the input video and creates subtitle for it using google API


* Download the model and scorer files from DeepSpeech repo And place it in main directory. The scorer file is optional, but it greatly improves inference results. 
    ```bash
    # Model file (~190 MB)
    $ wget https://github.com/mozilla/DeepSpeech/releases/download/v0.8.2/deepspeech-0.8.2-models.pbmm
    # Scorer file (~900 MB)
    $ wget https://github.com/mozilla/DeepSpeech/releases/download/v0.8.2/deepspeech-0.8.2-models.scorer
   
