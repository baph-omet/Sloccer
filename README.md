# Sloccer
A small Python script to get total SLOC in a directory.

## SLOC
SLOC, or Source Lines of Code, is a measure of the number of significant lines of code that are included in a source file. Basically, it's a rough measure of how much work you've put into a project. This script calculates SLOC a little different than GitHub. It basically ignores empty lines, comments, and lines with only opening/closing braces. Essentially, it counts the lines of code that actually have statements on them.

# Use
You'll need to have Python 3.4+ installed for this. 

1. Download the two `.py` files to wherever you want on your computer.

2. Edit `sloccer.py`, editing the `directory` variable at the top to the folder you want to scan, or leave it alone to use whatever directory the script is saved in. This way, you can just copy the script into whatever folder, and you're good to go. Note that it scans recursively.

3. Optionally, edit `languages.py` to add any entries for languages that you want to check. By default, I've added Java, C#, C++, JavaScript, Python, HTML, and CSS. All you need to do to add a new entry is create a new class in the following form:

Sample language class:

    class LanguageName(Default):
        enabled = True # True or False
        extension = "extension" # i.e. "java" for Java files or "cpp" for C++
        whitespace = [
          "comma",
          "separated",
          "list of whitespace",
          "characters"
        ]
        singleLineComment = [...] # same as above, but with whatever chars start single-line comments in this language
        
        multiLineCommentOpen = [...] # same as above, but with whatever chars start multi-line comments in this language
        
        multiLineCommentClose = [...] # same as above, but with whatever chars stop multi-line comments in this language
        
        ignore = [...] # same as above, but with a list of chars to ignore if they're alone on a line, i.e. brackets
        
Editing this file is optional, however, and is unnecessary for basic projects.

4. Run `sloccer.py` in Idle, Command Prompt, etc. and it'll spit out the SLOC for your project. Enjoy!
