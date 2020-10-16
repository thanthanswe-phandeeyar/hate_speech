# How to Run This

1. Download data from <crowdtangle.com>
2. Using the date range, name the file name in the format:
    - YYYYMMDD_YYYMMDD
3. Save the file under the directory:
   1. `data/crowdtangle-pages` for page data, and
   2. `data/crowdtangle-groups` for group data
4. Change the `json` file `src/_current_data_.json` properly
   1. For example, if you're processing group data for the date range 30 Apr, 2020-7 May 2020, change the json content as:

        ``` json
            {
                "pages_groups":"groups",
                "daterange":"20200430_20200507"
            }
        ```

5. Run scripts:
   1. `py_stage0_0_data_download.py`
   2. `py_stage0_1_data_download.py`
   3. `py_stage1_posts.py`
   4. `py_stage2_comments.py`
