#coding=utf-8
import os.path
import os


def path():
    print os.path.abspath("D:\\hello\\test")
    print os.path.basename("D:\\hello\\..\\test\\test.txt")
    print os.path.curdir
    paths = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/three/',
         ]
    print paths
    print os.path.commonprefix(paths)
    print os.path.dirname("D:\\hello\\test\\text.txt")
    
    print os.path.exists("D:\\hello\\test\\text.txt")
    print os.path.exists("D:\YouCam\YouCam")
    for user in [ '', 'dhellmann', 'postgres' ]:
        lookup = '~' + user
        print lookup, ':', os.path.expanduser(lookup)
        
    os.environ['MYVAR'] = 'VALUE'
    print os.path.expandvars('/path/to/$MYVAR')
    
    print os.path.getatime("D:\YouCam\YouCam")
    print os.path.getmtime("D:\YouCam\YouCam")
    print os.path.getctime("D:\YouCam\YouCam")
    print os.path.getsize("D:\YouCam\YouCam\Profile")
    print os.path.isabs("D:\YouCam\YouCam")
    print os.path.isabs("YouCam")
    print os.path.isfile("D:\YouCam\YouCam\Profile\WMV Best Quality.prx")
    print os.path.isdir("D:\YouCam\YouCam\Profile\WMV Best Quality.prx")
    print os.path.isdir("D:\YouCam\YouCam\Profile")
    print os.path.islink("D:\YouCam\YouCam\Profile")
    print os.path.ismount("D:\YouCam\YouCam\Profile")
    print os.path.join("D:\YouCam\YouCam\Profile", ("hello"))
    for parts in [ ('one', 'two', 'three'),
               ('/', 'one', 'two', 'three'),
               ('/one', '/two', '/three'),
               ]:
        print parts, ':', os.path.join(*parts)
    print os.path.normcase("D:\YouCam\.\YouCam\/dzsProfile")
    
    print os.path.normpath("D:\YouCam\.\YouCam\/dzsProfile")
    
    print os.path.realpath("D:\YouCam\YouCam\Profile\WMV Best Quality.prx")
    
    print os.path.relpath("D:\YouCam\YouCam","D:\YouCam")
    
    print os.path.relpath("E:\YouCam\YouCam")
    
    #print os.path.samefile("E:\YouCam\YouCam", "E:\YouCam\YouCam\Profile")
    #os.path.sameopenfile(fp1, fp2)
    #os.path.samestat(stat1, stat2)
    print os.path.split("E:\YouCam\YouCam")
    print os.path.splitdrive("E:\YouCam\YouCam")
    print os.path.splitext("D:\YouCam\YouCam\Profile\WMV Best Quality.prx")
    print os.path.splitunc(r"\YouCam\YouCam\Profile\WMV Best Quality.prx")
    
    def visit(arg, dirname, names):
        print dirname, arg
        for name in names:
            subname = os.path.join(dirname, name)
            if os.path.isdir(subname):
                print '  %s/' % name
            else:
                print '  %s' % name
        print
    
    print os.path.walk('example', visit, '(User data)')
if __name__ == '__main__':
    
    path()