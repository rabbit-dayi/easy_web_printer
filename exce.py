if __name__=='__main__':
    filepath="C:/3.pdf"
    import os
    run_command="python print.py "+filepath
    ex = os.popen(run_command)
    extext = ex.read()
    print(extext)
    ex.close()