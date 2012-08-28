'''
test_shared_hosting.py

Copyright 2012 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
'''

from ..helper import PluginTest, PluginConfig


class TestServerHeader(PluginTest):
    
    base_url = 'http://www.cybsec.com/'
    
    _run_configs = {
        'cfg': {
                'target': base_url,
                'plugins': {'infrastructure': (PluginConfig('shared_hosting'),)}
                }
        }
    
    def test_shared_hosting(self):
        cfg = self._run_configs['cfg']
        self._scan(cfg['target'], cfg['plugins'])
        
        domains = self.kb.getData('shared_hosting', 'domains')
        self.assertGreater( len(domains), 30, len(domains))
        
        infos = self.kb.getData('shared_hosting', 'shared_hosting')
        self.assertEqual( len(infos), 1, infos)
        
        info = infos[0]
        self.assertEqual('Shared hosting', info.getName() )
        
        