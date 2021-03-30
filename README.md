# Nautical Twilight
Repository for the 2021 PixelPad Game Jam.

### Contributing
The code in the repository is *formatted* for easier collaboration and legibility. 

### For Contributors
To format your .pp2d file, do the following:
- place your pp2d file in the **dataparse** directory. Any pp2d files there are automatically gitignored.
- run the inp.py script, with the syntax
`py inp.py pixpadfile outputfile`
- Name the output file source.txt, unless specified otherwise.
- This will automatically place the output file into the `source` directory.
- Changes can now be commited and pushed.

To change the source files into a useable .pp2d file, run the following:
`py out.py sourcefile pixelpadfile`
This will place a .pp2d file in the `dataparse` directory that you can now upload to the web to modify.
- In the commands, `pixelpadfile` must have the extension `.pp2d`.
- `outputfile` and `sourcefile` will almost always be named `source.txt`.

### For the public
- Follow the steps above, but `fork` the repository first. If you have made changes that you want to see in the base game, you're free to submit a **pull request**, but keep in mind that this project is pretty much done and pull requests will most likely be ignored.

### Conditions
- No liability or warranty is provided with distribution of this software. We in no way claim ownership of PixelPad engine or any of its affiliates.
