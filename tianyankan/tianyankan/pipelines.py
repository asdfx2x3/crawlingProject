# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os


class TianyankanPipeline(object):

    def process_item(self, item, spider):
        """

        :type item: object
        """
        cur_path = '/Users/ken/Documents/novels_date'

        temp_path = str(item['title'])
        target_path = cur_path + os.path.sep +temp_path
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        filename_path = cur_path + os.path.sep + str(item['title']) + os.path.sep + str(item['chap_name']) + '.txt'
        with open(filename_path, 'w', encoding='utf-8') as f:
            f.write(item['chap_content'])
            f.close()
        return item
