# Code-wars
My first mission from the code warriors.

This really took a lot outta me.2 days to be precise.
It seems that reversing a string is child play as compared to reversing the individual words in a string.
Who knows, some genius might use it in the future for some crazy encryption.
I started off by reversing the entire string and I saw that didn't give the desired output.
Then, by applying what really defines a word, I got it to reverse when ever it got to a whitespace.
This also turned out to be another problem since I now had to keep track of the changes and not reverse
the same words twice. Hence, a list... array... whatever was needed to store the changes.
Then special cases for punctuation marks since a word could also end with a punctuation mark. So I had to
take those into account as well. Also, we seem to have gotten to the point where we don't even end with punctuation 
marks so a special case had to be provided for that.

Long story short, the code has a lotta bugs and is not elegant at all.
But at least it gets the job done so I guess I shouldn't complain.
