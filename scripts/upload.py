import time
import os
import subprocess

# thanks to  http://mattmakesmaps.com/blog/2013/06/16/auto-push-to-github-via-machine-user/
out_data_parent_path = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))
out_data_path = os.path.join(out_data_parent_path, 'bl/blacklist*')

# Use suprocess module to push revised data to github.
# Need to set both the --git-dir and --work-tree
# http://stackoverflow.com/questions/1386291/git-git-dir-not-working-as-expected
subprocess.call(['git','--git-dir', out_data_parent_path + '/.git',
                 '--work-tree', out_data_parent_path,
                 'add', out_data_path])
subprocess.call(['git', '--git-dir', out_data_parent_path + '/.git',
                 '--work-tree', out_data_parent_path,
                 'commit', '-m', '"Blacklist Upload: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + '"'])
subprocess.call(['git', '--git-dir', out_data_parent_path + '/.git',
                 '--work-tree', out_data_parent_path,
                 'push'])
