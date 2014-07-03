# ansible-xml

[Ansible](http://www.ansible.com/home) module for manipulating bits
and pieces of XML files and strings.


# Notes

* This module is not 100% complete. No promises of support are made.

* **Pull requests are welcome!**

* This software is available under the terms of the GPLv2 license.

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

	xml: file=/foo/bar.xml xpath=/business/beers count=true
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

    xml: file=/foo/bar.xml xpath=/business/beers children={{ new_beers }}

The same, but do it inline

	xml:
	  file: /foo/bar.xml
	  xpath: /business/beers
	  children:
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
