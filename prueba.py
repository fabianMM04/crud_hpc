import subprocess
def ejecucion():
    cmd = ["condor_submit","foot.submit"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)

    out,err = p.communicate()
    return out

ejecucion()
