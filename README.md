# PySlice
 Python script for slicing audio files.

Requirements
 `> pip install pydub`

Parameters
   min_silence_len = The minimum duration of silence (in milliseconds) that is considered a “break” between slices.
   silence_thresh_db = The volume threshold (in decibels) below which the audio is considered “silent”.
   keep_silence = The number of milliseconds of silence to keep at the start and end of each slice.
