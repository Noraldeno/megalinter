# !/usr/bin/env python3
"""
Unit tests for REPOSITORY linter grype
This class has been automatically @generated by .automation/build.py, please don't update it manually
"""

from unittest import TestCase

from megalinter.tests.test_megalinter.LinterTestRoot import LinterTestRoot


class repository_grype_test(TestCase, LinterTestRoot):
    descriptor_id = "REPOSITORY"
    linter_name = "grype"
