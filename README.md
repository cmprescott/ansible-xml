[![Build Status](https://travis-ci.org/RHInception/ansible-xml.svg?branch=master)](https://travis-ci.org/RHInception/ansible-xml)
# ansible-xml

[Ansible](https://github.com/ansible/ansible) module for manipulating
bits and pieces of XML files and strings.

# Requirements

* Pythons bindings to ``libxml`` (usually in a package called
  ``python-lxml``, install with ``sudo apt-get install python-lxml``
  or ``sudo yum install python-lxml``).


# Notes

## We are giving up ownership of this module. This README will be updated with a notice once a new home is found

# Notes (cont...)

* This software is available under the terms of the GPLv2 license.
* Hi there, we have unit tests!

# What is XPath?

"XPath uses path expressions to select nodes or node-sets in an XML
document. The node is selected by following a path or steps."

Basically, it's a syntax which allows you to select a specific, or
collection, of elements or attributes in an XML file.

[Learn more at the Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/XPath)


# Unittests

Also included in this repository are
[Unittests](https://github.com/RHInception/ansible-xml/tree/master/tests). Reference
these, in addition to the
[Travis-CI](https://github.com/RHInception/ansible-xml/blob/master/.travis.yml)
configuration, if you need some more examples.


# Examples

Given:

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


Remove the ``subjective`` attribute of the rating element:

    xml: file=/foo/bar.xml xpath=/business/rating/@subjective ensure=absent

Set the rating to **11**

    xml: file=/foo/bar.xml xpath=/business/rating value=11

Get count of beers nodes

    xml: file=/foo/bar.xml xpath=/business/beers/beer count=true
      register: hits

    debug: var=hits.count



Add a ``phonenumber`` element to the ``business`` element Implicit
``mkdir -p`` behavior where applicable (parent xml nodes created
automatically)

    xml: file=/foo/bar.xml xpath=/business/phonenumber value=555-555-1234

Add several more beers to the beers element, assuming a **vars.yaml**
file with:

    new_beers:
        - beer: "Old Rasputin"
        - beer: "Old Motor Oil"
        - beer: "Old Curmudgeon"

Then the playbook syntax would look like this:

    xml: file=/foo/bar.xml xpath=/business/beers add_children={{ new_beers }}

The same, but do it inline

    xml:
      file: /foo/bar.xml
      xpath: /business/beers
      add_children:
          - beer: "Old Rasputin"
          - beer: "Old Motor Oil"
          - beer: "Old Curmudgeon"

Add a ``validxhtml`` element to the ``website`` element. Note that
``ensure`` is ``present`` by default, and ``value`` defaults to
``null`` for elements. The result is something like
``<website><validxhtml />...</website>``

    xml: file=/foo/bar.xml xpath=/business/website/validxhtml

Add an empty ``validatedon`` attribute to the ``validxhtml``
element. This actually makes the last example redundant because of the
implicit parent-node creation behavior. The result is something like
``<website><validxhtml validatedon='' />...</website>``

    xml: file=/foo/bar.xml xpath=/business/website/validxhtml/@validatedon

(1/2) Remove all children from the website element:

    xml: file=/foo/bar.xml xpath=/business/website/* ensure=absent

(2/2) Remove all children from the website element:

    xml:
      file: /foo/bar.xml
      xpath: /business/website
      children: []


Question? If You have ``<beers><child01 /><child02 /></beers>``

What happens if you say:

    xml: file=/foo/bar.xml xpath=/beers

``value`` defaults to an element, so then this would erase the
children elements.
