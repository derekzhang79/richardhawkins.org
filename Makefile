#RichardHawkins.org (My Website)
#Copyright (C) 2013 Richard Hawkins
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as
#published by the Free Software Foundation, either version 3 of the
#License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
SHELL=/bin/zsh -c

default:
	@echo "Starting dev server."
	@echo "Run 'make deploy' to deploy to Cloud Files"
	python run.py

deploy:
	python freeze.py
    # install https://github.com/gholt/swiftly
    # Add to .zshrc:
    #   swiftly-rh='swiftly --auth-url="https://identity.api.rackspacecloud.com/v2.0/" --auth-user="<username>" --auth-key="<apikey>" --region="<region>" "$@"'
	$(SHELL) 'swiftly-rh put richardhawkins.org -i website/build/'
