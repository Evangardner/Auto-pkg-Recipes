#!/usr/local/autopkg/python3.7
import os
import shutil

from autopkglib import Processor, ProcessorError

__all__ = ["DirectoryCreator"]

class DirectoryCreator(Processor):
    """Creates an empty directory at the specified path"""
    input_variables = {
        "name": {
            "required": True,
            "description": (
                "the name of the directory to be added."
            )
        },
        "path": {
            "required": True,
            "description": (
                "the path to the directory to be added, not including the new directory"
            )
        }
    }
    output_variables = {}
    description = __doc__

    def main(self):
            try:
                name = self.env["name"]
                path = self.env["path"]
                if os.path.exists(path):
                    dir = os.path.join(path, name)
                    os.mkdir(dir)
                elif not os.path.exists(path):
                    raise ProcessorError("path %s does not exist" % path)
                else:
                    raise ProcessorError("Could not add %s" % name)
                self.output("added directory %s at %s" % (name, path))
            except OSError as err:
                raise ProcessorError("Could not add to %s: %s" % (path, err))


if __name__ == "__main__":
    PROCESSOR = DirectoryCreator()
    PROCESSOR.execute_shell()
