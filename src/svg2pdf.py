import subprocess
import os



from_dir = os.path.join('.','svg')
to_dir = os.path.join('.','pdf')

for filenameExtension in os.listdir(from_dir):
    print(filenameExtension)
    filename, ext=os.path.splitext(filenameExtension)
    
    if os.name == 'posix':
        p=subprocess.call(['/usr/bin/inkscape', from_dir + '/' + filename + '.svg', '--export-pdf', to_dir + '/' + filename + '.pdf'])
    else:
        p=subprocess.call(['inkscape', from_dir + '\\' + filename + '.svg', '--export-pdf', to_dir + '\\' + filename + '.pdf'])
