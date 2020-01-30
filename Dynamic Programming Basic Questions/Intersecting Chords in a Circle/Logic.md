# Logic for the code given

Let there be  A chords given for a circle. We have to find the number of ways of putting these chords inside the circle such that these do 
not intersect. 

We have A chords (hence say, n=2A points on a cirlce). We have to start dividing the cricle such that no chord
intersects. If we take any 2 points on the circle( and make a chord out of them), then if there are 2k(say) points to the left of the chord
and 2(n-k-1) towards the right of the chord(there would be even number of points to the either side of the chord, think why ?). So total
ways of dividing the circle now are total ways in which these right 2n-2k-2 points can be used to divide the right half and total ways in which 
2k( left) points can divide the left half. So if ways(n)=ways(2k)*ways(2n-2k-2)

Now take 2 left most points ( such that the chord joining them towards the left most extreme of the circle, make drawing).
Towards the left of this chord are 0 points and towards the right of this chord are 2n-2 points.
So now when 2x0 (2k)=0 points are towards the left, then ways(n)=ways(2x0)*ways(2n-2x0-2). 

Hence for any k:- ways(n)=ways(2k)ways(2n-2k-2)...(1)

Now vary k from 0 to 2n-2 ( think why 2n-2 by putting 0 points to the right of right most point). Add every rhs in (1) accordingly to ways(n). You get
your result :) 






      







