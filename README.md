# Pi Audio Player

## Description
Pi project for playing random audio files (continuously) - except when connected via shairport-sync connection which overrides currently playing file. When shairport-sync session becomes inactive, random file playback resumes.

## Details

### Assumptions:

- Code assumes files are located under ``/audio`` (and playable by cvlc).
- Control file ``/tmp/airplay-playing`` generated by shairport-sync configuration.
- PulseAudio
- Tested on Raspberry Pi OS Bookworm

### Details:

Example build file and configuration for shairport-sync in ``build/build.sh`` and ``etc/shairport-sync.conf`` respectively.

Example ``systemd`` startup control files for both shairport-sync and the audio player: ``systemd/shairport-sync.service`` and ``systemd/playfile.service``



