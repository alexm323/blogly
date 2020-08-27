"""Seed file to make sample data for pets db."""

from models import *
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets

daft = User(first_name='Daft', last_name="Punk",
            image_url='https://upload.wikimedia.org/wikipedia/commons/4/41/Daftpunklapremiere2010.jpg')
anb = User(first_name='Above', last_name="& Beyond",
           image_url='https://d3vhc53cl8e8km.cloudfront.net/hello-staging/wp-content/uploads/2014/05/16183249/GiPAR5yJPIUvI0low4nSuuhewGIthxBqRcEj3ZZY-972x597.jpeg')
pink = User(first_name='Pink', last_name="Floyd",
            image_url='https://upload.wikimedia.org/wikipedia/en/d/d6/Pink_Floyd_-_all_members.jpg')
led = User(first_name='Led', last_name="Zeppelin",
           image_url='https://www.ledzeppelin.com/sites/g/files/g2000006376/f/201905/Led-Zeppelin-by-Dick-Barnatt---Redferns_London_December-1968_Getty-Images_3.jpg')
beatles = User(first_name='The', last_name="Beatles",
               image_url='https://upload.wikimedia.org/wikipedia/commons/d/df/The_Fabs.JPG')


# Add new objects to session, so they'll persist
db.session.add(daft)
db.session.add(anb)
db.session.add(pink)
db.session.add(led)
db.session.add(beatles)

# fed = Post(title='The Federalist', content='Defend the constitution',
#            created_at='July 4th, 1776', user_id=1)
discovery = Post(title='Discovery',
                 content='Discovery is the second studio album by French electronic music duo Daft Punk, released on 26 February 2001 by Virgin Records. It marks a shift from the Chicago house sound prevalent on their first studio record, Homework (1997), to a house style more heavily inspired by disco, post-disco, garage house, and R&B.', user_id=1)
darkside = Post(title='Dark Side of the Moon',
                content='The Dark Side of the Moon is the eighth studio album by English rock band Pink Floyd, released on 1 March 1973 by Harvest Records. Primarily developed during live performances, the band premiered an early version of the record several months before recording began.', user_id=3)
group = Post(title='Group Therapy',
             content='Group Therapy is the second studio album by British progressive trance group Above & Beyond. It was released on 6 June 2011 by Anjunabeats. The album features collaborations with Zoë Johnston and Richard Bedford', user_id=2)
iv = Post(title='Led Zeppelin IV',
                content='The untitled fourth studio album by the English rock band Led Zeppelin, commonly known as Led Zeppelin IV, was released on 8 November 1971 by Atlantic Records. It was produced by guitarist Jimmy Page and recorded between December 1970 and February 1971, mostly in the country house Headley Grange.', user_id=4)
animals = Post(title='Animals',
               content='Animals is the tenth studio album by English rock band Pink Floyd, released on 23 January 1977 through Harvest and Columbia Records. It was recorded at the bands Britannia Row Studios in London throughout 1976, and was produced by the band.', user_id=3)
abbey = Post(title='Abbey Road',
             content='Abbey Road is the eleventh studio album by the English rock band the Beatles, released on 26 September 1969 by Apple Records. Named after the location of EMI Studios in London, the cover features the group walking across the streets zebra crossing, an image that became one of the most famous and imitated in popular music. The albums initially mixed reviews were contrasted by its immediate commercial success, topping record charts in the UK and US. The lead single "Something" / "Come Together" was released in October and topped the US charts.', user_id=5)


# db.session.add(posts)
db.session.add(discovery)
db.session.add(darkside)
db.session.add(group)
db.session.add(iv)
db.session.add(animals)
db.session.add(abbey)

# Tag section

rock = Tag(name='Rock')
electronic = Tag(name='Electronic')
concept = Tag(name='Concept Rock')
psy = Tag(name='Psychedellic')

db.session.add(rock)
db.session.add(electronic)
db.session.add(concept)
db.session.add(psy)

# Tag section end


# Commit--otherwise, this never gets saved!
db.session.commit()

discovery_electronic = PostTag(post_id=1, tag_id=2)
animals_concept = PostTag(post_id=5, tag_id=3)
group_electronic = PostTag(post_id=3, tag_id=2)
dark_rock = PostTag(post_id=2, tag_id=1)
dark_psy = PostTag(post_id=2, tag_id=4)
dark_concept = PostTag(post_id=2, tag_id=3)
abbey_rock = PostTag(post_id=6, tag_id=1)
iv_rock = PostTag(post_id=4, tag_id=1)

db.session.add(discovery_electronic)
db.session.add(animals_concept)
db.session.add(group_electronic)
db.session.add(dark_rock)
db.session.add(dark_psy)
db.session.add(dark_concept)
db.session.add(abbey_rock)
db.session.add(iv_rock)

db.session.commit()
