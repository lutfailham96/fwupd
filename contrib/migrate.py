#!/usr/bin/python3
#
# Copyright (C) 2022 Richard Hughes <richard@hughsie.com>
#
# SPDX-License-Identifier: LGPL-2.1+
#

# import os
import sys
import glob


if __name__ == "__main__":

    fns = []

    if len(sys.argv) > 1:
        fns.extend(sys.argv[1:])
    else:
        exts = ["c", "h", "map"]
        for ext in exts:
            for fn in glob.glob("**/*.{}".format(ext), recursive=True):
                if fn.startswith("build"):
                    continue
                if fn.startswith("subprojects"):
                    continue
                if fn.startswith(".git"):
                    continue
                fns.append(fn)

    for fn in fns:
        modified: bool = False
        with open(fn, "r") as f:
            buf = f.read()
        for old, new in {
            "fu_common_sum8": "fu_sum8",
            "fu_common_sum8_bytes": "fu_sum8_bytes",
            "fu_common_sum16": "fu_sum16",
            "fu_common_sum16_bytes": "fu_sum16_bytes",
            "fu_common_sum16w": "fu_sum16w",
            "fu_common_sum16w_bytes": "fu_sum16w_bytes",
            "fu_common_sum32": "fu_sum32",
            "fu_common_sum32_bytes": "fu_sum32_bytes",
            "fu_common_sum32w": "fu_sum32w",
            "fu_common_sum32w_bytes": "fu_sum32w_bytes",
            "fu_common_crc8": "fu_crc8",
            "fu_common_crc8_full": "fu_crc8_full",
            "fu_common_crc16": "fu_crc16",
            "fu_common_crc16_full": "fu_crc16_full",
            "fu_common_crc32": "fu_crc32",
            "fu_common_crc32_full": "fu_crc32_full",
            "fu_common_string_replace": "fu_string_replace",
            "fu_common_string_append_kv": "fu_string_append",
            "fu_common_string_append_ku": "fu_string_append_ku",
            "fu_common_string_append_kx": "fu_string_append_kx",
            "fu_common_string_append_kb": "fu_string_append_kb",
            "fu_common_strnsplit": "fu_strsplit",
            "fu_common_strnsplit_full": "fu_strsplit_full",
            "fu_common_strjoin_array": "fu_strjoin",
            "fu_common_strsafe": "fu_strsafe",
            "fu_common_strwidth": "fu_strwidth",
            "fu_common_strstrip": "fu_strstrip",
            "fu_common_strtoull": "fu_strtoull",
            "fu_common_strtoull_full": "fu_strtoull_full",
            "FuCommonStrsplitFunc": "FuStrsplitFunc",
        }.items():
            if buf.find(old) == -1:
                continue
            buf = buf.replace(old, new)
            modified = True
        if modified:
            print("MODIFIED: {}".format(fn))
            with open(fn, "w") as f:
                f.write(buf)

    sys.exit(0)