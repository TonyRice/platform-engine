# -*- coding: utf-8 -*-
import time

from .Handler import Handler
from ..Stories import Stories


class Story:

    @staticmethod
    def story(logger, app_id, story_name):
        return Stories(logger, app_id, story_name)

    @staticmethod
    def save(config, logger, story, start):
        """
        Saves the narration and the results for each line.
        """
        logger.log('story-save', story.name, story.app_id)
        mongo = Handler.init_mongo(config.mongo)
        mongo_story = mongo.story(story.name, story.app_id)
        narration = mongo.narration(mongo_story, story, story.version, start,
                                    time.time())
        mongo.lines(narration, story.results)

    @staticmethod
    def execute(config, logger, story):
        """
        Executes each line in the story
        """
        line_number = '1'
        while line_number:
            line_number = Handler.run(logger, line_number, story)
            if line_number:
                if line_number.endswith('.story'):
                    line_number = Story.run(config, logger, story.app_id,
                                            line_number)

    @classmethod
    def run(cls, config, logger, app_id, story_name, *, story_id=None):
        logger.log('story-start', story_name, app_id, story_id)
        start = time.time()
        story = cls.story(logger, app_id, story_name)
        story.get()
        cls.execute(config, logger, story)
        cls.save(config, logger, story, start)
        logger.log('story-end', story_name, app_id, story_id)