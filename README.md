## Coding Challenge - Python 3.6
### Fork repo. With `listings.txt` and `products.txt` in same directory as `final.py`: `python final.py`
##### About Me:
Since brevity is ~~the soul of~~ wit, I will keep this short and sweet. I have always been a problem solver. I spend all my free time tinkering and learning about how stuff works. Whether it's getting my hands dirty repairing my bike or hours of keyboard clacking to fix a bug, I always relish the opportunity to problem solve because I know I will finish that much more prepared for the next problem.
I have a post-graduate education, but not one in math, engineering or computer science. However, I am capable of the kind of thinking those fields require. At the very least, when I explore a new field or subject--and its respective challenges and problems--I invariably learn to excel because I ask questions, I get peer's input and I have fun with it.
<!-- from approaching table to reading blog
inc knowledge of cameras like  camera_check -->
<!-- I have always been a problem solver. In som
I don't have a formal background in math, engineering or computer science, but my what my experience does demonstrate is an ability to quickly learn how things work and apply that knowledge in a practical and productive way.

I have always been able to take a subject, teach myself the fundamental skills, learn from experts and excel in that subject:
- I was interested in politics so I did a BA in political science and eventually worked on political campaigns and became an editor at my university's newspaper.
- I was interested in photography, I read books practiced and learned from peers. Eventually I won a national photography award and worked breifly as a freelance photo-journalist
- I was interested in journalism, so I started writing stories for my university's paper, became an editor and did research for some of Canada's most prominent journalists.

why hire someon w/o degrees - learn fast enuf to excel in interests. they are all actually problem solving.
So why hire someone whose interest jumps around so much? Well all these interests seem diverse, they have two very essential things in common: A fascination with how things work and an ability to apply knowledge of how those things work.

When I learned how to drive I became fascinated with all its elements and eventually got a job at an auto-parts company.
I don't have a math, computer science or engineering degree. I don't see that
I'm sure there are much more elegant solutions to this problem, but if anything my being able to solve this with a limited knowledge of Python speaks to my ability to really -->
##### Process/Approach:
My experience with Python before this challenge was limited to 4-5 hours a couple months ago, so I was going to try and keep things simple. It may have been wiser to use a language I was comfortable with, but I had been looking for an excuse to get some Python practice and I thought if ever there was a time to do it, it was while completing a coding challenge for a company that uses it.
Before actually planning my approach I just kicked the tires a bit and made a **rough** list of the 3 categories of listings and their unique and/or possibly problematic  characteristics:
1. Camera with Accessories:
   - **Could:**
     - have camera of Product, but also had accessories with their own names and models--creating the potential for false or missed matches.
   - **Often:**
     - included `+`, `mm`, `with` in  `title`
2. Just Camera:
   - **Could:**
     - have `family`. If `family` was not a key, then the family was **often** included in `product_name`
     - have `model` that was substring of another `model` or an unrelated part of the listing `title`
3. Just accessories(never to be in listings of product):
   - **Often:**
     - contained `model` of product
   - **Usually:**
     - made by manufacturers not included in products

I then mapped the relationships between listing's and product's key/value pairs. From there I just started writing out basic `if` statements and testing results, usually printing a group of listings with loose relationships to products and seeing if it matched listings that my method had not caught: e.g. printing any listing containing the product's manufacturer and the first two digits of the model and making sure I hadn't missed any. I will be the first to admit this was probably not the most elegant way to work through it, but I planned based on my inexperience with Python.
After refining my approach down a bit I then tested product listings for duplicates and added in a few lines to prevent them (see below).
Below is a flow chart that more or less demonstrates my approach to generating matches.
![Optional Text](../master/sortable_flow.png)
Speed was my biggest challenge. I tried to mitigate speed issues by using some of Python docs' suggestion (e.g. using local over global variables, avoiding nested functions that generate undue overhead, etc). I also filtered `listings` starting with less laborious `if` statements and incorporated the more taxing ones once other possibilities had been eliminated. I also included a step that removed all listings that have been added to a `results` hash from the array of searchable listings, which both avoided duplicates and made the search for products progressively faster. I also originally used a `while` loop for the products, but switched to `for`, which reduced the time by about 67%.  
I was initially worried about memory, but after some research I discovered that Python's garbage collection is pretty conducive to my approach and would probably cover me. More specifically, because Products that have been checked already are dictionaries (i.e. mutable objects), Python can let them go once they are no longer referenced. I did read 
At any rate, I certainly could have refactored more, but I kept the `if` statements for a two important reasons:
1. They give the code an "under-the-hood" kind of readability.
2. Python can evaluate an `if` statement faster than it can call/execute a function, generally speaking.

#### Problems/Solutions:
Solved = [x]
There were a lot of ways that false matches could be generated, solvable with varying degrees of ease. Here are a couple:
- [x] Listings with different model formatting than Product e.g. `Olympus vg120` vs. `Olympus vg-120`
    * Creating a function that split numbers and letters of model with a `-` with regex
- [x] Substring of `Camera A1` matches `Camera A123`
    * Simply adding a space to the end of the product_name, such that it would only match with Listing titles that were that substring (after the title was reformatted with spaces instead of `-`,`,` or `_`)
- [x] Model_name of Product was included in unrelated part `title` of `Listing` e.g. `model: 400` vs. `camera ABC ... 400 X 600`
    * Because this only occurred with model names that were just numbers--with the exception of 3 model names (`zoom`,`slice`,`tryx`) which I confirmed were matched correctly--if it was trying to generate a match using a `model` that was just digits, it would verify that that `model` was contained in the first 4 words of the `title`.
- [x] Listings that were only accessories slipping through the cracks
    * Some listings that were _only_ accessories were actually made by the same manufacturers as the Products, so I wrote crude but effective function. It searches those accessories, checking whether they had some of the characteristics that kits have but just accessories don't and filtered them out accordingly (e.g. `+`,which are only in listings that are kits; `mm`, which are only listed with lenses; `with`, which is the same case as `+`)
- [x] Duplicates: I created a test to identify duplicates before finishing, of which there were a few.
- [ ] Efficiency: It's possible my method of creating an array of listings to iterate over is the most efficient way of doing things. It was just an easy way to prevent duplicates and give the method a 25% speed boost. In retrospect, a set() probably would've been a better choice.
##### Improvements:
It would be fun to try and incorporate some of the other info given in the products/listings to sort them. For example, the likelihood that a product has a listing with certain identifiers changes based on the `announced-date` of the product. For example, until a few years ago, high-end cameras usually used CF cards and others used SD cards.
I don't really have anything in the way of experience with sorting algorithms, but I'm sure with a basic introduction to them I could figure out a better way to do this. Moreover, there were some cool sorting modules that I wish I had known about when I started(e.g. `heapq`).
