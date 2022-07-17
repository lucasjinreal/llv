# from llv.converter.mixamodae2json import load_mixamodae_as_json
import sys

import json


if __name__ == "__main__":
    # load_mixamodae_as_json(sys.argv[1])

    frames_content = json.load(open("data_clip1.json", "r"))
    for fs in frames_content:
        print(fs)
        dfs = json.loads(fs)

        b = json.dumps(dfs)

        print(b)
        print(b.encode())




