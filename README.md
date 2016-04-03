Ncs-wells
=========

[View page](http://ivarref.github.io/ncs-wells/).

Goal
-----
Show cumulative discoveries vs. number of cumulative wells drilled.

About the data
--------------
The wellbores are collected from the Wellbore NPD page: Table view -> Exploration -> All - long list.
Only wellbores with purpose 'WILDCAT' is processed further.

These wells are mapped to reserves on the "Field NPD page: Table view -> Reserves"
and "Discovery NPD page: Table view -> Resources".

Update
------

    git clone git@github.com:ivarref/ncs-wells.git && \
    cd ncs-wells && ./pull_data.py && \
    git commit -am "$(date): update data" && git push && \
    git checkout gh-pages && git merge master && git push

Comments
--------
refsdal.ivar@gmail.com

