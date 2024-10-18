import requests
import os
import glob

class HLSDownloader:
    @staticmethod
    def download_track_from_hls(url: str) -> None:
        # download the .m3u8 playlist and parse it
        m3u8_content = requests.get(url).text
        segment_urls = [line for line in m3u8_content.splitlines() if line and not line.startswith("#")]

        if not os.path.exists('segments'):
            os.makedirs('segments')

        # download all segments
        for i, segment_url in enumerate(segment_urls):
            segment_data = requests.get(segment_url).content
            with open(f"segments/segment_{i}.ts", "wb") as segment_file:
                segment_file.write(segment_data)

        print("All segments downloaded!")

        with open('file_list.txt', 'w') as f:
            for i in range(len(segment_urls)):
                f.write(f"file '{os.path.abspath(f'segments/segment_{i}.ts')}'\n")

        # combine the segments
        ffmpeg_command = "ffmpeg -f concat -safe 0 -i file_list.txt -c copy output.mp3"
        os.system(ffmpeg_command)

        print("Segments combined into output.mp3!")

        files = glob.glob('segments/*.ts')
        for f in files:
            os.remove(f)
        os.remove('file_list.txt')

        print("Cleanup done")


# SoundCloudDownloader.download_track_from_hls("https://cf-hls-media.sndcdn.com/playlist/ClyiS27VOaRv.128.mp3/playlist.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiKjovL2NmLWhscy1tZWRpYS5zbmRjZG4uY29tL3BsYXlsaXN0L0NseWlTMjdWT2FSdi4xMjgubXAzL3BsYXlsaXN0Lm0zdTgqIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzI4ODQ0NTY0fX19XX0_&Signature=RO08cEXoXac1KuOQUMsYWKSBO0fRg1ltXQml7HvLgP3KuVVcuBpxexDPB5AI4itP8iq6UDlJoK-HMMyV8pEdaG7Ug-C8eOkzCDdsHibvOQomAgQF~zmgZUT-uW6U-K4AenYh0yM2N9WZXlNPdL-ceipFxnck9~Md-2LLl3VuIvbtBXjkpygmr1hU2qgg3QMgyLUIzUawohF0oAtmOhxnLpYHvKvKwEJBo9tp7YiDrzgvSbOibXOiS-ytPf4bEhgUg7ejRmPgOH-S2Nrjn7i7GWwCoxJsSwjUgpdW~FUCJPTVMk8C8D0Evd17LfCOFrLnXZFP-jZ8lC-0bDTqK2jhsg__&Key-Pair-Id=APKAI6TU7MMXM5DG6EPQ")