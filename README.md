[![Build Status][travis_badge]][travis_results]
# ansible-xml

[Ansible][src_ansible] module for manipulating bits and pieces of XML files and strings. This module is currently in devel version of [Ansible][github_repo_ansible]. It should be released as part of Ansible 2.4.0 in [Mid-September](https://github.com/ansible/ansible/blob/devel/docs/docsite/rst/roadmap/ROADMAP_2_4.rst). As a consequence, all the issues should be reported to [ansible](https://github.com/ansible/ansible/issues).

# Installation

* This module requires Python bindings to ``libxml`` version 2.3 or later. This is usually in a package called 
  ``python-lxml``. Install with ``apt-get install python-lxml``, ``yum install python-lxml``, or ``pip install lxml``.
* This module is **NOT** included with Ansible v2.3 and below. Install with ``git clone https://github.com/cmprescott/ansible-xml.git``,
  or ``ansible-galaxy install cmprescott.xml``. Valid installation paths are 
  [the playbook's library directory][doc_install_in_playbook], 
  [the playbook's roles directory and include in the playbook][doc_install_as_role], 
  or [Ansible's modules path][doc_install_in_path].

# Notes

* Original module created by [@github_rhinception][github_team_rhinception].
* On 2015-05-05, [@tbielawa][github_user_tbielawa] transferred the project over to [@cmprescott][github_user_cmprescott] to resolve [issue #16][github_issue_16].
* On 2017-08-08, this module was merged upstream into [Ansible][github_repo_ansible].
* This software is available under the terms of the GPLv3 license.
* Hi there, we have unit tests!

# What is XPath?

"XPath uses path expressions to select nodes or node-sets in an XML
document. The node is selected by following a path or steps."

Basically, it's a syntax which allows you to select a specific, or
collection, of elements or attributes in an XML file.

[Learn more at the Mozilla Developer Network][doc_xpath]


# Unittests

Also included in this repository are
[Unittests][src_this_unittests]. Reference these, in addition to the
[Travis-CI][src_this_travis] configuration, if you need some more examples.


# Examples

Given:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<business type="bar">
    <name>Tasty Beverage Co.</name>
    <beers>
        <beer>Rochefort 10</beer>
        <beer>St. Bernardus Abbot 12</beer>
        <beer>Schlitz</beer>
    </beers>
    <rating subjective="true">10</rating>
    <website>
        <mobilefriendly />
        <address>http://tastybeverageco.com</address>
    </website>
</business>
```

Remove the ``subjective`` attribute of the rating element:

```yaml
xml:
  path: /foo/bar.xml
  xpath: /business/rating/@subjective
  state: absent
```

Set the rating to **11**

```yaml
xml:
  path: /foo/bar.xml
  xpath: /business/rating
  value: 11
```

Get count of beers nodes

```yaml
xml:
  path: /foo/bar.xml
  xpath: /business/beers/beer
  count: yes
register: hits

debug:
  var: hits.count
```


Add a ``phonenumber`` element to the ``business`` element Implicit
``mkdir -p`` behavior where applicable (parent xml nodes created
automatically)

```yaml
xml:
  path: /foo/bar.xml
  xpath: /business/phonenumber
  value: 555-555-1234
```

Add several more beers to the beers element, assuming a **vars.yaml**
file with:

```yaml
new_beers:
    - beer: "Old Rasputin"
    - beer: "Old Motor Oil"
    - beer: "Old Curmudgeon"
```

Then the playbook syntax would look like this:

```yaml
xml:
  path: /foo/bar.xml
  xpath: /business/beers
  add_children: '{{ new_beers }}'
```

The same, but do it inline

```yaml
xml:
  path: /foo/bar.xml
  xpath: /business/beers
  add_children:
      - beer: "Old Rasputin"
      - beer: "Old Motor Oil"
      - beer: "Old Curmudgeon"
```

Add a ``validxhtml`` element to the ``website`` element. Note that
``state`` is ``present`` by default, and ``value`` defaults to
``null`` for elements. The result is something like
``<website><validxhtml />...</website>``

```yaml
xml:
  path: /foo/bar.xml
  xpath: /business/website/validxhtml
```

Add an empty ``validatedon`` attribute to the ``validxhtml``
element. This actually makes the last example redundant because of the
implicit parent-node creation behavior. The result is something like
``<website><validxhtml validatedon='' />...</website>``

```yaml
xml:
  path: /foo/bar.xml
  xpath: /business/website/validxhtml/@validatedon
```

(1/2) Remove all children from the website element:

```yaml
xml:
  path: /foo/bar.xml
  xpath: /business/website/*
  state: absent
```

(2/2) Remove all children from the website element:

```yaml
xml:
  path: /foo/bar.xml
  xpath: /business/website
  children: []
```

Question? If You have ``<beers><child01 /><child02 /></beers>``

What happens if you say:

```yaml
xml:
  path: /foo/bar.xml
  xpath: /beers
```

``value`` defaults to an element, so then this would erase the
children elements.

[doc_xpath]: https://developer.mozilla.org/en-US/docs/Web/XPath
[doc_install_as_role]: http://docs.ansible.com/ansible/playbooks_roles.html#embedding-modules-and-plugins-in-roles
[doc_install_in_path]: http://docs.ansible.com/ansible/developing_modules.html#module-paths
[doc_install_in_playbook]: http://docs.ansible.com/ansible/playbooks_best_practices.html#bundling-ansible-modules-with-playbooks
[github_issue_16]: https://github.com/cmprescott/ansible-xml/issues/16
[github_repo_ansible]: https://github.com/ansible/ansible
[github_user_cmprescott]: https://github.com/cmprescott
[github_user_tbielawa]: https://github.com/tbielawa
[github_team_rhinception]: https://github.com/RHInception
[src_ansible]: https://github.com/ansible/ansible
[src_this_travis]: https://github.com/cmprescott/ansible-xml/blob/master/.travis.yml
[src_this_unittests]: https://github.com/cmprescott/ansible-xml/tree/master/tests
[travis_badge]: https://travis-ci.org/cmprescott/ansible-xml.svg?branch=master
[travis_results]: https://travis-ci.org/cmprescott/ansible-xml
