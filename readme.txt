label generator
by AutoRaccoon

This tool is free to use, but I always welcome donations here:
https://www.buymeacoffee.com/autoraccoon

**************************************
label generator is a basic mail merger tool made in native python2 (python3 from 0.3)
it only needs python to run

****************************************

It was build to generate different svg files as label for different products from a main template.
As SVG files are XML, it can read from any text file. in practice.
It can be used to replace specific text from any text template

It needs a template (XML file, including but not limited to svg) and a csv file to work.
The tool looks for specific bits of text in the template and replaces them by the content in the csv.
It then outputs one file from each row of the csv (excluding the title one) in the output directory
Make sure that the template, the generator and the csv are in the next directory, else it won't work.
*************************************

instructions:

make template
run gen
enter the name of the template
enter name of csv

***USE EXE IN DIST FOLDER TO USE WITHOUT PYTHON INSTALL***

each text to be replaced must be written as "%VAR_text%", and each corresponding column in the csv must be named "text". nb: text is a variable, the column name is the value of the 1st row of the column
ex: if a template contains %VAR_name% and the csv has a column with the value "name" on the first row (the column name), Anna on the 2nd row and Mark on 3rd row, the generator will output one file where "%Var_text%" will be replaced by "Anna" and another where it will be replaced by Mark.
The first column or the csv will be used to determine the names of the generated output files.
Last version is 0.2
