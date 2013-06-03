Sync NIST's National Vulnerability Database with Jira
=====================================================

The 'nvdsync' utility wraps the
'[nvd2sqlite3](https://github.com/jschauma/nvd2sqlite3)' and
'[nvdXjira](https://github.com/jschauma/nvdXjira)' tools to provide a
simple script suitable to be run from a cronjob in order to fetch NIST's
National Vulnerability Database, sync it into a local sqlite3 database and
then cross-reference that database with a Jira instance.

Who wrote this tool?
--------------------
'nvdXjira' was originally written by Jan Schaumann (jschauma@netmeister.org) in
May 2013.
