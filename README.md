# Sound Downloader For Soundcloud
A simple class which can be extended to download souncloud music. The function can download and combine a m8u8 playlist. 🔊

The function will be updated to take links for soudcloud songs, but for not its main functionality is downloading the song from the hls link that is fetched from an internal api by souncloud.

## Example Usage: ##
code:
<pre>
  HLSDownloader.download_track_from_hls("https://cf-hls-media.sndcdn.com/playlist/ClyiS27VOaRv.128.mp3/playlist.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiKjovL2NmLWhscy1tZWRpYS5zbmRjZG4uY29tL3BsYXlsaXN0L0NseWlTMjdWT2FSdi4xMjgubXAzL3BsYXlsaXN0Lm0zdTgqIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzI4ODQ0NTY0fX19XX0_&Signature=RO08cEXoXac1KuOQUMsYWKSBO0fRg1ltXQml7HvLgP3KuVVcuBpxexDPB5AI4itP8iq6UDlJoK-HMMyV8pEdaG7Ug-C8eOkzCDdsHibvOQomAgQF~zmgZUT-uW6U-K4AenYh0yM2N9WZXlNPdL-ceipFxnck9~Md-2LLl3VuIvbtBXjkpygmr1hU2qgg3QMgyLUIzUawohF0oAtmOhxnLpYHvKvKwEJBo9tp7YiDrzgvSbOibXOiS-ytPf4bEhgUg7ejRmPgOH-S2Nrjn7i7GWwCoxJsSwjUgpdW~FUCJPTVMk8C8D0Evd17LfCOFrLnXZFP-jZ8lC-0bDTqK2jhsg__&Key-Pair-Id=APKAI6TU7MMXM5DG6EPQ")
</pre>

output:
-> a .mp3 file in the current working directory with the full song

## Dependencies ##
• Requires ffmpeg to be installed locally (a built-in  will be added to remove the need for this) 🎛️ <br />
• Requires the python `requests` library 🌐 
