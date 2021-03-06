# Ansible Development: Best way to get at CIDR netmask data? (i.e. "/24" rather than 255.255.255.0)
# https://groups.google.com/forum/#!topic/ansible-devel/vyXjlsHYCQ8

# Adapted from:
# http://code.activestate.com/recipes/576483-convert-subnetmask-from-cidr-notation-to-dotdecima/

# Convert a dotted (xxx.xxx.xxx.xxx) netmask to CIDR bits (xx) notation
def netmask_to_cidr(netmask):
    return sum([bin(int(x)).count('1') for x in netmask.split('.')])

class FilterModule(object):
    ''' utility filters for operating on ip netmasks '''

    def filters(self):
        return {
            'netmask_to_cidr' : netmask_to_cidr
        }
