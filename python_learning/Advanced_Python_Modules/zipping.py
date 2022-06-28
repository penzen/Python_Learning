# zip files are compressed files 
import zipfile
import shutil # extracts and zips whole folders 
f = open('fileone.txt','w+')
f.write("Hello monkeys it looks like a wonderfull day")
f.close()
 

f = open('filetwo.txt','w+')
f.write("Hello monkeys it looks like a wonderfull day")
f.close()

# create the zip file 

comp_file = zipfile.ZipFile('Comp_file.zip','w') # makes a zip file zip
comp_file.write('fileone.txt',compress_type = zipfile.ZIP_DEFLATED) 
comp_file.write('filetwo.txt',compress_type = zipfile.ZIP_DEFLATED) 
comp_file.close()

# unzipping file is
zip_obj = zipfile.ZipFile('Comp_file.zip','r')
zip_obj.extractall('extracted_content') # creates folders for the extracted zip files 

# zip an entire folder 
dir_to_zip = 'c:\\Users\\penze\\OneDrive\\Desktop\\python_learning\\extracted_content'
output = 'example'
shutil.make_archive(output, 'zip',dir_to_zip,)

# unzip an entir folder 
shutil.unpack_archive('example.zip','final_unzip','zip')
# grabs the fileone and then compress it to the Comp_file.zip tab 
