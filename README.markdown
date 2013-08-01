RichardHawkins.org
==================

My website.


Setup
-----
1. Setup swiftly
  - install https://github.com/gholt/swiftly
  - echo 'swiftly --auth-url="https://identity.api.rackspacecloud.com/v2.0/" --auth-user="<username>" --auth-key="<apikey>" --region="<region>" "$@"' > ~/bin/swiftly-rh
  - chmod u+x ~/bin/swiftly-rh
  - Ensure ~/bin is in your path.

2. Create container for site.
  - swiftly-rh put richardhawkins.org -h'X-Container-Meta-Web-Index: index.html' -h'X-Container-Meta-Web-Error: error.html'
  - swiftly-rh --cdn put richardhawkins.org -h'X-Cdn-Enabled: True' -h'X-Ttl: 900' -h'X-Log-Retention: True'

3. Install required python modules
  - pip install -r requirements.txt

4. make deploy
