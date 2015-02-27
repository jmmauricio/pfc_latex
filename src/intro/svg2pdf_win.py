import subprocess
import os



from_dir = os.path.join('.','svg')
to_dir = os.path.join('.','pdf')

print os.getcwd()
for filenameExtension in os.listdir(from_dir):
    print filenameExtension
    filename, ext=os.path.splitext(filenameExtension)
    from_file = os.path.join(os.getcwd(),'svg','{:s}.svg'.format(filename))
    to_file =os.path.join(os.getcwd(),'pdf','{:s}.pdf'.format(filename))
    print from_file
                             
    p=subprocess.call([r'C:\Program Files (x86)\Inkscape\inkscape.exe', from_file, '--export-pdf', to_file])
    print to_file

