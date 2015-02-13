from fabric.api import run

def bind(foreman, surveyor):
    surveyor['os'] = determine_os


HOST_IDENTIFIERS = {
    "":""
}

def determine_os(survey):
    result = {
        'platform': "",
        'distribution': "",
        'version': "",
        'name': ""
    }
    
    result['platform'] = run('python -c "import platform; print platform.system()"')
    
    # for linux distributions, determine the distribution details
    if result['platform'] == 'Linux':
        distro = run('python -c "import platform; print platform.linux_distribution()"')[1:-1].split(",")
        distname, version, name = [d.strip() for d in distro]
        result['distribution'] = distname
        result['version'] = version
        result['name'] = name
        
    return result