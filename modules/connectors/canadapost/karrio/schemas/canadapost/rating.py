#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Jul 14 15:39:45 2021 by generateDS.py version 2.39.2.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './canadapost_lib/rating.py')
#
# Command line arguments:
#   ./schemas/rating.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-carriers/.venv/karrio-carriers/bin/generateDS --no-namespace-defs -o "./canadapost_lib/rating.py" ./schemas/rating.xsd
#
# Current working directory (os.getcwd()):
#   canadapost
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class quote_typeType(str, Enum):
    COMMERCIAL='commercial'
    COUNTER='counter'


class mailing_scenario(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, customer_number=None, contract_id=None, promo_code=None, quote_type=None, expected_mailing_date=None, options=None, parcel_characteristics=None, services=None, origin_postal_code=None, destination=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customer_number = customer_number
        self.customer_number_nsprefix_ = None
        self.contract_id = contract_id
        self.contract_id_nsprefix_ = None
        self.promo_code = promo_code
        self.validate_PromoCodeType(self.promo_code)
        self.promo_code_nsprefix_ = None
        self.quote_type = quote_type
        self.validate_quote_typeType(self.quote_type)
        self.quote_type_nsprefix_ = None
        if isinstance(expected_mailing_date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(expected_mailing_date, '%Y-%m-%d').date()
        else:
            initvalue_ = expected_mailing_date
        self.expected_mailing_date = initvalue_
        self.expected_mailing_date_nsprefix_ = None
        self.options = options
        self.options_nsprefix_ = None
        self.parcel_characteristics = parcel_characteristics
        self.parcel_characteristics_nsprefix_ = None
        self.services = services
        self.services_nsprefix_ = None
        self.origin_postal_code = origin_postal_code
        self.origin_postal_code_nsprefix_ = None
        self.destination = destination
        self.destination_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, mailing_scenario)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if mailing_scenario.subclass:
            return mailing_scenario.subclass(*args_, **kwargs_)
        else:
            return mailing_scenario(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_customer_number(self):
        return self.customer_number
    def set_customer_number(self, customer_number):
        self.customer_number = customer_number
    def get_contract_id(self):
        return self.contract_id
    def set_contract_id(self, contract_id):
        self.contract_id = contract_id
    def get_promo_code(self):
        return self.promo_code
    def set_promo_code(self, promo_code):
        self.promo_code = promo_code
    def get_quote_type(self):
        return self.quote_type
    def set_quote_type(self, quote_type):
        self.quote_type = quote_type
    def get_expected_mailing_date(self):
        return self.expected_mailing_date
    def set_expected_mailing_date(self, expected_mailing_date):
        self.expected_mailing_date = expected_mailing_date
    def get_options(self):
        return self.options
    def set_options(self, options):
        self.options = options
    def get_parcel_characteristics(self):
        return self.parcel_characteristics
    def set_parcel_characteristics(self, parcel_characteristics):
        self.parcel_characteristics = parcel_characteristics
    def get_services(self):
        return self.services
    def set_services(self, services):
        self.services = services
    def get_origin_postal_code(self):
        return self.origin_postal_code
    def set_origin_postal_code(self, origin_postal_code):
        self.origin_postal_code = origin_postal_code
    def get_destination(self):
        return self.destination
    def set_destination(self, destination):
        self.destination = destination
    def validate_PromoCodeType(self, value):
        result = True
        # Validate type PromoCodeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PromoCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PromoCodeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_quote_typeType(self, value):
        result = True
        # Validate type quote-typeType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['commercial', 'counter']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on quote-typeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.customer_number is not None or
            self.contract_id is not None or
            self.promo_code is not None or
            self.quote_type is not None or
            self.expected_mailing_date is not None or
            self.options is not None or
            self.parcel_characteristics is not None or
            self.services is not None or
            self.origin_postal_code is not None or
            self.destination is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='mailing-scenario', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('mailing-scenario')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'mailing-scenario':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='mailing-scenario')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='mailing-scenario', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='mailing-scenario'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='mailing-scenario', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.customer_number is not None:
            namespaceprefix_ = self.customer_number_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-number>%s</%scustomer-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_number), input_name='customer-number')), namespaceprefix_ , eol_))
        if self.contract_id is not None:
            namespaceprefix_ = self.contract_id_nsprefix_ + ':' if (UseCapturedNS_ and self.contract_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontract-id>%s</%scontract-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contract_id), input_name='contract-id')), namespaceprefix_ , eol_))
        if self.promo_code is not None:
            namespaceprefix_ = self.promo_code_nsprefix_ + ':' if (UseCapturedNS_ and self.promo_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spromo-code>%s</%spromo-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.promo_code), input_name='promo-code')), namespaceprefix_ , eol_))
        if self.quote_type is not None:
            namespaceprefix_ = self.quote_type_nsprefix_ + ':' if (UseCapturedNS_ and self.quote_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%squote-type>%s</%squote-type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.quote_type), input_name='quote-type')), namespaceprefix_ , eol_))
        if self.expected_mailing_date is not None:
            namespaceprefix_ = self.expected_mailing_date_nsprefix_ + ':' if (UseCapturedNS_ and self.expected_mailing_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexpected-mailing-date>%s</%sexpected-mailing-date>%s' % (namespaceprefix_ , self.gds_format_date(self.expected_mailing_date, input_name='expected-mailing-date'), namespaceprefix_ , eol_))
        if self.options is not None:
            namespaceprefix_ = self.options_nsprefix_ + ':' if (UseCapturedNS_ and self.options_nsprefix_) else ''
            self.options.export(outfile, level, namespaceprefix_, namespacedef_='', name_='options', pretty_print=pretty_print)
        if self.parcel_characteristics is not None:
            namespaceprefix_ = self.parcel_characteristics_nsprefix_ + ':' if (UseCapturedNS_ and self.parcel_characteristics_nsprefix_) else ''
            self.parcel_characteristics.export(outfile, level, namespaceprefix_, namespacedef_='', name_='parcel-characteristics', pretty_print=pretty_print)
        if self.services is not None:
            namespaceprefix_ = self.services_nsprefix_ + ':' if (UseCapturedNS_ and self.services_nsprefix_) else ''
            self.services.export(outfile, level, namespaceprefix_, namespacedef_='', name_='services', pretty_print=pretty_print)
        if self.origin_postal_code is not None:
            namespaceprefix_ = self.origin_postal_code_nsprefix_ + ':' if (UseCapturedNS_ and self.origin_postal_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sorigin-postal-code>%s</%sorigin-postal-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.origin_postal_code), input_name='origin-postal-code')), namespaceprefix_ , eol_))
        if self.destination is not None:
            namespaceprefix_ = self.destination_nsprefix_ + ':' if (UseCapturedNS_ and self.destination_nsprefix_) else ''
            self.destination.export(outfile, level, namespaceprefix_, namespacedef_='', name_='destination', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'customer-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customer_number')
            value_ = self.gds_validate_string(value_, node, 'customer_number')
            self.customer_number = value_
            self.customer_number_nsprefix_ = child_.prefix
        elif nodeName_ == 'contract-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contract_id')
            value_ = self.gds_validate_string(value_, node, 'contract_id')
            self.contract_id = value_
            self.contract_id_nsprefix_ = child_.prefix
        elif nodeName_ == 'promo-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'promo_code')
            value_ = self.gds_validate_string(value_, node, 'promo_code')
            self.promo_code = value_
            self.promo_code_nsprefix_ = child_.prefix
            # validate type PromoCodeType
            self.validate_PromoCodeType(self.promo_code)
        elif nodeName_ == 'quote-type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'quote_type')
            value_ = self.gds_validate_string(value_, node, 'quote_type')
            self.quote_type = value_
            self.quote_type_nsprefix_ = child_.prefix
            # validate type quote-typeType
            self.validate_quote_typeType(self.quote_type)
        elif nodeName_ == 'expected-mailing-date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.expected_mailing_date = dval_
            self.expected_mailing_date_nsprefix_ = child_.prefix
        elif nodeName_ == 'options':
            obj_ = optionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.options = obj_
            obj_.original_tagname_ = 'options'
        elif nodeName_ == 'parcel-characteristics':
            obj_ = parcel_characteristicsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.parcel_characteristics = obj_
            obj_.original_tagname_ = 'parcel-characteristics'
        elif nodeName_ == 'services':
            obj_ = servicesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.services = obj_
            obj_.original_tagname_ = 'services'
        elif nodeName_ == 'origin-postal-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'origin_postal_code')
            value_ = self.gds_validate_string(value_, node, 'origin_postal_code')
            self.origin_postal_code = value_
            self.origin_postal_code_nsprefix_ = child_.prefix
        elif nodeName_ == 'destination':
            obj_ = destinationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.destination = obj_
            obj_.original_tagname_ = 'destination'
# end class mailing_scenario


class price_quotes(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, price_quote=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if price_quote is None:
            self.price_quote = []
        else:
            self.price_quote = price_quote
        self.price_quote_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, price_quotes)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if price_quotes.subclass:
            return price_quotes.subclass(*args_, **kwargs_)
        else:
            return price_quotes(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_price_quote(self):
        return self.price_quote
    def set_price_quote(self, price_quote):
        self.price_quote = price_quote
    def add_price_quote(self, value):
        self.price_quote.append(value)
    def insert_price_quote_at(self, index, value):
        self.price_quote.insert(index, value)
    def replace_price_quote_at(self, index, value):
        self.price_quote[index] = value
    def _hasContent(self):
        if (
            self.price_quote
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='price-quotes', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('price-quotes')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'price-quotes':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='price-quotes')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='price-quotes', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='price-quotes'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='price-quotes', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for price_quote_ in self.price_quote:
            namespaceprefix_ = self.price_quote_nsprefix_ + ':' if (UseCapturedNS_ and self.price_quote_nsprefix_) else ''
            price_quote_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='price-quote', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'price-quote':
            obj_ = price_quoteType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.price_quote.append(obj_)
            obj_.original_tagname_ = 'price-quote'
# end class price_quotes


class TaxType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, percent=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.percent = _cast(float, percent)
        self.percent_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TaxType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TaxType.subclass:
            return TaxType.subclass(*args_, **kwargs_)
        else:
            return TaxType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_percent(self):
        return self.percent
    def set_percent(self, percent):
        self.percent = percent
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TaxType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TaxType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TaxType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TaxType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TaxType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TaxType'):
        if self.percent is not None and 'percent' not in already_processed:
            already_processed.add('percent')
            outfile.write(' percent="%s"' % self.gds_format_decimal(self.percent, input_name='percent'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TaxType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('percent', node)
        if value is not None and 'percent' not in already_processed:
            already_processed.add('percent')
            value = self.gds_parse_decimal(value, node, 'percent')
            self.percent = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TaxType


class optionsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, option=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if option is None:
            self.option = []
        else:
            self.option = option
        self.option_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, optionsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if optionsType.subclass:
            return optionsType.subclass(*args_, **kwargs_)
        else:
            return optionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_option(self):
        return self.option
    def set_option(self, option):
        self.option = option
    def add_option(self, value):
        self.option.append(value)
    def insert_option_at(self, index, value):
        self.option.insert(index, value)
    def replace_option_at(self, index, value):
        self.option[index] = value
    def _hasContent(self):
        if (
            self.option
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='optionsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('optionsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'optionsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='optionsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='optionsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='optionsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='optionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for option_ in self.option:
            namespaceprefix_ = self.option_nsprefix_ + ':' if (UseCapturedNS_ and self.option_nsprefix_) else ''
            option_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='option', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'option':
            obj_ = optionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.option.append(obj_)
            obj_.original_tagname_ = 'option'
# end class optionsType


class optionType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, option_code=None, option_amount=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.option_code = option_code
        self.validate_option_codeType(self.option_code)
        self.option_code_nsprefix_ = None
        self.option_amount = option_amount
        self.option_amount_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, optionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if optionType.subclass:
            return optionType.subclass(*args_, **kwargs_)
        else:
            return optionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_option_code(self):
        return self.option_code
    def set_option_code(self, option_code):
        self.option_code = option_code
    def get_option_amount(self):
        return self.option_amount
    def set_option_amount(self, option_amount):
        self.option_amount = option_amount
    def validate_option_codeType(self, value):
        result = True
        # Validate type option-codeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on option-codeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on option-codeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.option_code is not None or
            self.option_amount is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='optionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('optionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'optionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='optionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='optionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='optionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='optionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.option_code is not None:
            namespaceprefix_ = self.option_code_nsprefix_ + ':' if (UseCapturedNS_ and self.option_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-code>%s</%soption-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.option_code), input_name='option-code')), namespaceprefix_ , eol_))
        if self.option_amount is not None:
            namespaceprefix_ = self.option_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.option_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-amount>%s</%soption-amount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.option_amount), input_name='option-amount')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'option-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'option_code')
            value_ = self.gds_validate_string(value_, node, 'option_code')
            self.option_code = value_
            self.option_code_nsprefix_ = child_.prefix
            # validate type option-codeType
            self.validate_option_codeType(self.option_code)
        elif nodeName_ == 'option-amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'option_amount')
            value_ = self.gds_validate_string(value_, node, 'option_amount')
            self.option_amount = value_
            self.option_amount_nsprefix_ = child_.prefix
# end class optionType


class parcel_characteristicsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, weight=None, dimensions=None, unpackaged=None, mailing_tube=None, oversized=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.weight = weight
        self.validate_weightType(self.weight)
        self.weight_nsprefix_ = None
        self.dimensions = dimensions
        self.dimensions_nsprefix_ = None
        self.unpackaged = unpackaged
        self.unpackaged_nsprefix_ = None
        self.mailing_tube = mailing_tube
        self.mailing_tube_nsprefix_ = None
        self.oversized = oversized
        self.oversized_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, parcel_characteristicsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if parcel_characteristicsType.subclass:
            return parcel_characteristicsType.subclass(*args_, **kwargs_)
        else:
            return parcel_characteristicsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_weight(self):
        return self.weight
    def set_weight(self, weight):
        self.weight = weight
    def get_dimensions(self):
        return self.dimensions
    def set_dimensions(self, dimensions):
        self.dimensions = dimensions
    def get_unpackaged(self):
        return self.unpackaged
    def set_unpackaged(self, unpackaged):
        self.unpackaged = unpackaged
    def get_mailing_tube(self):
        return self.mailing_tube
    def set_mailing_tube(self, mailing_tube):
        self.mailing_tube = mailing_tube
    def get_oversized(self):
        return self.oversized
    def set_oversized(self, oversized):
        self.oversized = oversized
    def validate_weightType(self, value):
        result = True
        # Validate type weightType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value > 99.999:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on weightType' % {"value": value, "lineno": lineno} )
                result = False
            if value <= 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minExclusive restriction on weightType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.weight is not None or
            self.dimensions is not None or
            self.unpackaged is not None or
            self.mailing_tube is not None or
            self.oversized is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='parcel-characteristicsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('parcel-characteristicsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'parcel-characteristicsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='parcel-characteristicsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='parcel-characteristicsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='parcel-characteristicsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='parcel-characteristicsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.weight is not None:
            namespaceprefix_ = self.weight_nsprefix_ + ':' if (UseCapturedNS_ and self.weight_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sweight>%s</%sweight>%s' % (namespaceprefix_ , self.gds_format_decimal(self.weight, input_name='weight'), namespaceprefix_ , eol_))
        if self.dimensions is not None:
            namespaceprefix_ = self.dimensions_nsprefix_ + ':' if (UseCapturedNS_ and self.dimensions_nsprefix_) else ''
            self.dimensions.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dimensions', pretty_print=pretty_print)
        if self.unpackaged is not None:
            namespaceprefix_ = self.unpackaged_nsprefix_ + ':' if (UseCapturedNS_ and self.unpackaged_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunpackaged>%s</%sunpackaged>%s' % (namespaceprefix_ , self.gds_format_boolean(self.unpackaged, input_name='unpackaged'), namespaceprefix_ , eol_))
        if self.mailing_tube is not None:
            namespaceprefix_ = self.mailing_tube_nsprefix_ + ':' if (UseCapturedNS_ and self.mailing_tube_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smailing-tube>%s</%smailing-tube>%s' % (namespaceprefix_ , self.gds_format_boolean(self.mailing_tube, input_name='mailing-tube'), namespaceprefix_ , eol_))
        if self.oversized is not None:
            namespaceprefix_ = self.oversized_nsprefix_ + ':' if (UseCapturedNS_ and self.oversized_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soversized>%s</%soversized>%s' % (namespaceprefix_ , self.gds_format_boolean(self.oversized, input_name='oversized'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'weight' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'weight')
            fval_ = self.gds_validate_decimal(fval_, node, 'weight')
            self.weight = fval_
            self.weight_nsprefix_ = child_.prefix
            # validate type weightType
            self.validate_weightType(self.weight)
        elif nodeName_ == 'dimensions':
            obj_ = dimensionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dimensions = obj_
            obj_.original_tagname_ = 'dimensions'
        elif nodeName_ == 'unpackaged':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'unpackaged')
            ival_ = self.gds_validate_boolean(ival_, node, 'unpackaged')
            self.unpackaged = ival_
            self.unpackaged_nsprefix_ = child_.prefix
        elif nodeName_ == 'mailing-tube':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'mailing_tube')
            ival_ = self.gds_validate_boolean(ival_, node, 'mailing_tube')
            self.mailing_tube = ival_
            self.mailing_tube_nsprefix_ = child_.prefix
        elif nodeName_ == 'oversized':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'oversized')
            ival_ = self.gds_validate_boolean(ival_, node, 'oversized')
            self.oversized = ival_
            self.oversized_nsprefix_ = child_.prefix
# end class parcel_characteristicsType


class dimensionsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, length=None, width=None, height=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.length = length
        self.length_nsprefix_ = None
        self.width = width
        self.width_nsprefix_ = None
        self.height = height
        self.height_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dimensionsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dimensionsType.subclass:
            return dimensionsType.subclass(*args_, **kwargs_)
        else:
            return dimensionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_length(self):
        return self.length
    def set_length(self, length):
        self.length = length
    def get_width(self):
        return self.width
    def set_width(self, width):
        self.width = width
    def get_height(self):
        return self.height
    def set_height(self, height):
        self.height = height
    def _hasContent(self):
        if (
            self.length is not None or
            self.width is not None or
            self.height is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='dimensionsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dimensionsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dimensionsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dimensionsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dimensionsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dimensionsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='dimensionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.length is not None:
            namespaceprefix_ = self.length_nsprefix_ + ':' if (UseCapturedNS_ and self.length_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slength>%s</%slength>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.length), input_name='length')), namespaceprefix_ , eol_))
        if self.width is not None:
            namespaceprefix_ = self.width_nsprefix_ + ':' if (UseCapturedNS_ and self.width_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%swidth>%s</%swidth>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.width), input_name='width')), namespaceprefix_ , eol_))
        if self.height is not None:
            namespaceprefix_ = self.height_nsprefix_ + ':' if (UseCapturedNS_ and self.height_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sheight>%s</%sheight>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.height), input_name='height')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'length':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'length')
            value_ = self.gds_validate_string(value_, node, 'length')
            self.length = value_
            self.length_nsprefix_ = child_.prefix
        elif nodeName_ == 'width':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'width')
            value_ = self.gds_validate_string(value_, node, 'width')
            self.width = value_
            self.width_nsprefix_ = child_.prefix
        elif nodeName_ == 'height':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'height')
            value_ = self.gds_validate_string(value_, node, 'height')
            self.height = value_
            self.height_nsprefix_ = child_.prefix
# end class dimensionsType


class servicesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if service_code is None:
            self.service_code = []
        else:
            self.service_code = service_code
        self.service_code_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, servicesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if servicesType.subclass:
            return servicesType.subclass(*args_, **kwargs_)
        else:
            return servicesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_service_code(self):
        return self.service_code
    def set_service_code(self, service_code):
        self.service_code = service_code
    def add_service_code(self, value):
        self.service_code.append(value)
    def insert_service_code_at(self, index, value):
        self.service_code.insert(index, value)
    def replace_service_code_at(self, index, value):
        self.service_code[index] = value
    def _hasContent(self):
        if (
            self.service_code
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='servicesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('servicesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'servicesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='servicesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='servicesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='servicesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='servicesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for service_code_ in self.service_code:
            namespaceprefix_ = self.service_code_nsprefix_ + ':' if (UseCapturedNS_ and self.service_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-code>%s</%sservice-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(service_code_), input_name='service-code')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'service-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'service_code')
            value_ = self.gds_validate_string(value_, node, 'service_code')
            self.service_code.append(value_)
            self.service_code_nsprefix_ = child_.prefix
# end class servicesType


class destinationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, domestic=None, united_states=None, international=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.domestic = domestic
        self.domestic_nsprefix_ = None
        self.united_states = united_states
        self.united_states_nsprefix_ = None
        self.international = international
        self.international_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, destinationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if destinationType.subclass:
            return destinationType.subclass(*args_, **kwargs_)
        else:
            return destinationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_domestic(self):
        return self.domestic
    def set_domestic(self, domestic):
        self.domestic = domestic
    def get_united_states(self):
        return self.united_states
    def set_united_states(self, united_states):
        self.united_states = united_states
    def get_international(self):
        return self.international
    def set_international(self, international):
        self.international = international
    def _hasContent(self):
        if (
            self.domestic is not None or
            self.united_states is not None or
            self.international is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='destinationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('destinationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'destinationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='destinationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='destinationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='destinationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='destinationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.domestic is not None:
            namespaceprefix_ = self.domestic_nsprefix_ + ':' if (UseCapturedNS_ and self.domestic_nsprefix_) else ''
            self.domestic.export(outfile, level, namespaceprefix_, namespacedef_='', name_='domestic', pretty_print=pretty_print)
        if self.united_states is not None:
            namespaceprefix_ = self.united_states_nsprefix_ + ':' if (UseCapturedNS_ and self.united_states_nsprefix_) else ''
            self.united_states.export(outfile, level, namespaceprefix_, namespacedef_='', name_='united-states', pretty_print=pretty_print)
        if self.international is not None:
            namespaceprefix_ = self.international_nsprefix_ + ':' if (UseCapturedNS_ and self.international_nsprefix_) else ''
            self.international.export(outfile, level, namespaceprefix_, namespacedef_='', name_='international', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'domestic':
            obj_ = domesticType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.domestic = obj_
            obj_.original_tagname_ = 'domestic'
        elif nodeName_ == 'united-states':
            obj_ = united_statesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.united_states = obj_
            obj_.original_tagname_ = 'united-states'
        elif nodeName_ == 'international':
            obj_ = internationalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.international = obj_
            obj_.original_tagname_ = 'international'
# end class destinationType


class domesticType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, postal_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.postal_code = postal_code
        self.postal_code_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, domesticType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if domesticType.subclass:
            return domesticType.subclass(*args_, **kwargs_)
        else:
            return domesticType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_postal_code(self):
        return self.postal_code
    def set_postal_code(self, postal_code):
        self.postal_code = postal_code
    def _hasContent(self):
        if (
            self.postal_code is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='domesticType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('domesticType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'domesticType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='domesticType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='domesticType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='domesticType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='domesticType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.postal_code is not None:
            namespaceprefix_ = self.postal_code_nsprefix_ + ':' if (UseCapturedNS_ and self.postal_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostal-code>%s</%spostal-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.postal_code), input_name='postal-code')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'postal-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postal_code')
            value_ = self.gds_validate_string(value_, node, 'postal_code')
            self.postal_code = value_
            self.postal_code_nsprefix_ = child_.prefix
# end class domesticType


class united_statesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, zip_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.zip_code = zip_code
        self.zip_code_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, united_statesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if united_statesType.subclass:
            return united_statesType.subclass(*args_, **kwargs_)
        else:
            return united_statesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_zip_code(self):
        return self.zip_code
    def set_zip_code(self, zip_code):
        self.zip_code = zip_code
    def _hasContent(self):
        if (
            self.zip_code is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='united-statesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('united-statesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'united-statesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='united-statesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='united-statesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='united-statesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='united-statesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.zip_code is not None:
            namespaceprefix_ = self.zip_code_nsprefix_ + ':' if (UseCapturedNS_ and self.zip_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szip-code>%s</%szip-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.zip_code), input_name='zip-code')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'zip-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'zip_code')
            value_ = self.gds_validate_string(value_, node, 'zip_code')
            self.zip_code = value_
            self.zip_code_nsprefix_ = child_.prefix
# end class united_statesType


class internationalType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, country_code=None, postal_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.country_code = country_code
        self.country_code_nsprefix_ = None
        self.postal_code = postal_code
        self.validate_IntlPostalCodeType(self.postal_code)
        self.postal_code_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, internationalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if internationalType.subclass:
            return internationalType.subclass(*args_, **kwargs_)
        else:
            return internationalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_country_code(self):
        return self.country_code
    def set_country_code(self, country_code):
        self.country_code = country_code
    def get_postal_code(self):
        return self.postal_code
    def set_postal_code(self, postal_code):
        self.postal_code = postal_code
    def validate_IntlPostalCodeType(self, value):
        result = True
        # Validate type IntlPostalCodeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on IntlPostalCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on IntlPostalCodeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.country_code is not None or
            self.postal_code is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='internationalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('internationalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'internationalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='internationalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='internationalType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='internationalType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='internationalType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.country_code is not None:
            namespaceprefix_ = self.country_code_nsprefix_ + ':' if (UseCapturedNS_ and self.country_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountry-code>%s</%scountry-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.country_code), input_name='country-code')), namespaceprefix_ , eol_))
        if self.postal_code is not None:
            namespaceprefix_ = self.postal_code_nsprefix_ + ':' if (UseCapturedNS_ and self.postal_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostal-code>%s</%spostal-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.postal_code), input_name='postal-code')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'country-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'country_code')
            value_ = self.gds_validate_string(value_, node, 'country_code')
            self.country_code = value_
            self.country_code_nsprefix_ = child_.prefix
        elif nodeName_ == 'postal-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postal_code')
            value_ = self.gds_validate_string(value_, node, 'postal_code')
            self.postal_code = value_
            self.postal_code_nsprefix_ = child_.prefix
            # validate type IntlPostalCodeType
            self.validate_IntlPostalCodeType(self.postal_code)
# end class internationalType


class price_quoteType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service_code=None, service_link=None, service_name=None, price_details=None, weight_details=None, service_standard=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.service_code = service_code
        self.service_code_nsprefix_ = None
        self.service_link = service_link
        self.service_link_nsprefix_ = None
        self.service_name = service_name
        self.service_name_nsprefix_ = None
        self.price_details = price_details
        self.price_details_nsprefix_ = None
        self.weight_details = weight_details
        self.weight_details_nsprefix_ = None
        self.service_standard = service_standard
        self.service_standard_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, price_quoteType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if price_quoteType.subclass:
            return price_quoteType.subclass(*args_, **kwargs_)
        else:
            return price_quoteType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_service_code(self):
        return self.service_code
    def set_service_code(self, service_code):
        self.service_code = service_code
    def get_service_link(self):
        return self.service_link
    def set_service_link(self, service_link):
        self.service_link = service_link
    def get_service_name(self):
        return self.service_name
    def set_service_name(self, service_name):
        self.service_name = service_name
    def get_price_details(self):
        return self.price_details
    def set_price_details(self, price_details):
        self.price_details = price_details
    def get_weight_details(self):
        return self.weight_details
    def set_weight_details(self, weight_details):
        self.weight_details = weight_details
    def get_service_standard(self):
        return self.service_standard
    def set_service_standard(self, service_standard):
        self.service_standard = service_standard
    def _hasContent(self):
        if (
            self.service_code is not None or
            self.service_link is not None or
            self.service_name is not None or
            self.price_details is not None or
            self.weight_details is not None or
            self.service_standard is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='price-quoteType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('price-quoteType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'price-quoteType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='price-quoteType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='price-quoteType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='price-quoteType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='price-quoteType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.service_code is not None:
            namespaceprefix_ = self.service_code_nsprefix_ + ':' if (UseCapturedNS_ and self.service_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-code>%s</%sservice-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_code), input_name='service-code')), namespaceprefix_ , eol_))
        if self.service_link is not None:
            namespaceprefix_ = self.service_link_nsprefix_ + ':' if (UseCapturedNS_ and self.service_link_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-link>%s</%sservice-link>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_link), input_name='service-link')), namespaceprefix_ , eol_))
        if self.service_name is not None:
            namespaceprefix_ = self.service_name_nsprefix_ + ':' if (UseCapturedNS_ and self.service_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-name>%s</%sservice-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_name), input_name='service-name')), namespaceprefix_ , eol_))
        if self.price_details is not None:
            namespaceprefix_ = self.price_details_nsprefix_ + ':' if (UseCapturedNS_ and self.price_details_nsprefix_) else ''
            self.price_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='price-details', pretty_print=pretty_print)
        if self.weight_details is not None:
            namespaceprefix_ = self.weight_details_nsprefix_ + ':' if (UseCapturedNS_ and self.weight_details_nsprefix_) else ''
            self.weight_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='weight-details', pretty_print=pretty_print)
        if self.service_standard is not None:
            namespaceprefix_ = self.service_standard_nsprefix_ + ':' if (UseCapturedNS_ and self.service_standard_nsprefix_) else ''
            self.service_standard.export(outfile, level, namespaceprefix_, namespacedef_='', name_='service-standard', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'service-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'service_code')
            value_ = self.gds_validate_string(value_, node, 'service_code')
            self.service_code = value_
            self.service_code_nsprefix_ = child_.prefix
        elif nodeName_ == 'service-link':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'service_link')
            value_ = self.gds_validate_string(value_, node, 'service_link')
            self.service_link = value_
            self.service_link_nsprefix_ = child_.prefix
        elif nodeName_ == 'service-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'service_name')
            value_ = self.gds_validate_string(value_, node, 'service_name')
            self.service_name = value_
            self.service_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'price-details':
            obj_ = price_detailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.price_details = obj_
            obj_.original_tagname_ = 'price-details'
        elif nodeName_ == 'weight-details':
            obj_ = weight_detailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.weight_details = obj_
            obj_.original_tagname_ = 'weight-details'
        elif nodeName_ == 'service-standard':
            obj_ = service_standardType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.service_standard = obj_
            obj_.original_tagname_ = 'service-standard'
# end class price_quoteType


class price_detailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, base=None, taxes=None, due=None, options=None, adjustments=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.base = base
        self.base_nsprefix_ = None
        self.taxes = taxes
        self.taxes_nsprefix_ = None
        self.due = due
        self.due_nsprefix_ = None
        self.options = options
        self.options_nsprefix_ = None
        self.adjustments = adjustments
        self.adjustments_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, price_detailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if price_detailsType.subclass:
            return price_detailsType.subclass(*args_, **kwargs_)
        else:
            return price_detailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_base(self):
        return self.base
    def set_base(self, base):
        self.base = base
    def get_taxes(self):
        return self.taxes
    def set_taxes(self, taxes):
        self.taxes = taxes
    def get_due(self):
        return self.due
    def set_due(self, due):
        self.due = due
    def get_options(self):
        return self.options
    def set_options(self, options):
        self.options = options
    def get_adjustments(self):
        return self.adjustments
    def set_adjustments(self, adjustments):
        self.adjustments = adjustments
    def _hasContent(self):
        if (
            self.base is not None or
            self.taxes is not None or
            self.due is not None or
            self.options is not None or
            self.adjustments is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='price-detailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('price-detailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'price-detailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='price-detailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='price-detailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='price-detailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='price-detailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.base is not None:
            namespaceprefix_ = self.base_nsprefix_ + ':' if (UseCapturedNS_ and self.base_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbase>%s</%sbase>%s' % (namespaceprefix_ , self.gds_format_decimal(self.base, input_name='base'), namespaceprefix_ , eol_))
        if self.taxes is not None:
            namespaceprefix_ = self.taxes_nsprefix_ + ':' if (UseCapturedNS_ and self.taxes_nsprefix_) else ''
            self.taxes.export(outfile, level, namespaceprefix_, namespacedef_='', name_='taxes', pretty_print=pretty_print)
        if self.due is not None:
            namespaceprefix_ = self.due_nsprefix_ + ':' if (UseCapturedNS_ and self.due_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdue>%s</%sdue>%s' % (namespaceprefix_ , self.gds_format_decimal(self.due, input_name='due'), namespaceprefix_ , eol_))
        if self.options is not None:
            namespaceprefix_ = self.options_nsprefix_ + ':' if (UseCapturedNS_ and self.options_nsprefix_) else ''
            self.options.export(outfile, level, namespaceprefix_, namespacedef_='', name_='options', pretty_print=pretty_print)
        if self.adjustments is not None:
            namespaceprefix_ = self.adjustments_nsprefix_ + ':' if (UseCapturedNS_ and self.adjustments_nsprefix_) else ''
            self.adjustments.export(outfile, level, namespaceprefix_, namespacedef_='', name_='adjustments', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'base' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'base')
            fval_ = self.gds_validate_decimal(fval_, node, 'base')
            self.base = fval_
            self.base_nsprefix_ = child_.prefix
        elif nodeName_ == 'taxes':
            obj_ = taxesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.taxes = obj_
            obj_.original_tagname_ = 'taxes'
        elif nodeName_ == 'due' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'due')
            fval_ = self.gds_validate_decimal(fval_, node, 'due')
            self.due = fval_
            self.due_nsprefix_ = child_.prefix
        elif nodeName_ == 'options':
            obj_ = optionsType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.options = obj_
            obj_.original_tagname_ = 'options'
        elif nodeName_ == 'adjustments':
            obj_ = adjustmentsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.adjustments = obj_
            obj_.original_tagname_ = 'adjustments'
# end class price_detailsType


class taxesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gst=None, pst=None, hst=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.gst = gst
        self.gst_nsprefix_ = None
        self.pst = pst
        self.pst_nsprefix_ = None
        self.hst = hst
        self.hst_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, taxesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if taxesType.subclass:
            return taxesType.subclass(*args_, **kwargs_)
        else:
            return taxesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_gst(self):
        return self.gst
    def set_gst(self, gst):
        self.gst = gst
    def get_pst(self):
        return self.pst
    def set_pst(self, pst):
        self.pst = pst
    def get_hst(self):
        return self.hst
    def set_hst(self, hst):
        self.hst = hst
    def _hasContent(self):
        if (
            self.gst is not None or
            self.pst is not None or
            self.hst is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='taxesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('taxesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'taxesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='taxesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='taxesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='taxesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='taxesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.gst is not None:
            namespaceprefix_ = self.gst_nsprefix_ + ':' if (UseCapturedNS_ and self.gst_nsprefix_) else ''
            self.gst.export(outfile, level, namespaceprefix_, namespacedef_='', name_='gst', pretty_print=pretty_print)
        if self.pst is not None:
            namespaceprefix_ = self.pst_nsprefix_ + ':' if (UseCapturedNS_ and self.pst_nsprefix_) else ''
            self.pst.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pst', pretty_print=pretty_print)
        if self.hst is not None:
            namespaceprefix_ = self.hst_nsprefix_ + ':' if (UseCapturedNS_ and self.hst_nsprefix_) else ''
            self.hst.export(outfile, level, namespaceprefix_, namespacedef_='', name_='hst', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'gst':
            obj_ = TaxType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.gst = obj_
            obj_.original_tagname_ = 'gst'
        elif nodeName_ == 'pst':
            obj_ = TaxType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pst = obj_
            obj_.original_tagname_ = 'pst'
        elif nodeName_ == 'hst':
            obj_ = TaxType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.hst = obj_
            obj_.original_tagname_ = 'hst'
# end class taxesType


class optionsType1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, option=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if option is None:
            self.option = []
        else:
            self.option = option
        self.option_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, optionsType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if optionsType1.subclass:
            return optionsType1.subclass(*args_, **kwargs_)
        else:
            return optionsType1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_option(self):
        return self.option
    def set_option(self, option):
        self.option = option
    def add_option(self, value):
        self.option.append(value)
    def insert_option_at(self, index, value):
        self.option.insert(index, value)
    def replace_option_at(self, index, value):
        self.option[index] = value
    def _hasContent(self):
        if (
            self.option
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='optionsType1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('optionsType1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'optionsType1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='optionsType1')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='optionsType1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='optionsType1'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='optionsType1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for option_ in self.option:
            namespaceprefix_ = self.option_nsprefix_ + ':' if (UseCapturedNS_ and self.option_nsprefix_) else ''
            option_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='option', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'option':
            obj_ = optionType2.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.option.append(obj_)
            obj_.original_tagname_ = 'option'
# end class optionsType1


class optionType2(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, option_code=None, option_name=None, option_price=None, qualifier=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.option_code = option_code
        self.option_code_nsprefix_ = None
        self.option_name = option_name
        self.option_name_nsprefix_ = None
        self.option_price = option_price
        self.option_price_nsprefix_ = None
        self.qualifier = qualifier
        self.qualifier_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, optionType2)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if optionType2.subclass:
            return optionType2.subclass(*args_, **kwargs_)
        else:
            return optionType2(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_option_code(self):
        return self.option_code
    def set_option_code(self, option_code):
        self.option_code = option_code
    def get_option_name(self):
        return self.option_name
    def set_option_name(self, option_name):
        self.option_name = option_name
    def get_option_price(self):
        return self.option_price
    def set_option_price(self, option_price):
        self.option_price = option_price
    def get_qualifier(self):
        return self.qualifier
    def set_qualifier(self, qualifier):
        self.qualifier = qualifier
    def _hasContent(self):
        if (
            self.option_code is not None or
            self.option_name is not None or
            self.option_price is not None or
            self.qualifier is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='optionType2', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('optionType2')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'optionType2':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='optionType2')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='optionType2', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='optionType2'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='optionType2', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.option_code is not None:
            namespaceprefix_ = self.option_code_nsprefix_ + ':' if (UseCapturedNS_ and self.option_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-code>%s</%soption-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.option_code), input_name='option-code')), namespaceprefix_ , eol_))
        if self.option_name is not None:
            namespaceprefix_ = self.option_name_nsprefix_ + ':' if (UseCapturedNS_ and self.option_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-name>%s</%soption-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.option_name), input_name='option-name')), namespaceprefix_ , eol_))
        if self.option_price is not None:
            namespaceprefix_ = self.option_price_nsprefix_ + ':' if (UseCapturedNS_ and self.option_price_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-price>%s</%soption-price>%s' % (namespaceprefix_ , self.gds_format_decimal(self.option_price, input_name='option-price'), namespaceprefix_ , eol_))
        if self.qualifier is not None:
            namespaceprefix_ = self.qualifier_nsprefix_ + ':' if (UseCapturedNS_ and self.qualifier_nsprefix_) else ''
            self.qualifier.export(outfile, level, namespaceprefix_, namespacedef_='', name_='qualifier', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'option-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'option_code')
            value_ = self.gds_validate_string(value_, node, 'option_code')
            self.option_code = value_
            self.option_code_nsprefix_ = child_.prefix
        elif nodeName_ == 'option-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'option_name')
            value_ = self.gds_validate_string(value_, node, 'option_name')
            self.option_name = value_
            self.option_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'option-price' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'option_price')
            fval_ = self.gds_validate_decimal(fval_, node, 'option_price')
            self.option_price = fval_
            self.option_price_nsprefix_ = child_.prefix
        elif nodeName_ == 'qualifier':
            obj_ = qualifierType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.qualifier = obj_
            obj_.original_tagname_ = 'qualifier'
# end class optionType2


class qualifierType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, step_size=None, step_cost=None, included_amount=None, max_value=None, included=None, percent=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.step_size = step_size
        self.step_size_nsprefix_ = None
        self.step_cost = step_cost
        self.step_cost_nsprefix_ = None
        self.included_amount = included_amount
        self.included_amount_nsprefix_ = None
        self.max_value = max_value
        self.max_value_nsprefix_ = None
        self.included = included
        self.included_nsprefix_ = None
        self.percent = percent
        self.percent_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, qualifierType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if qualifierType.subclass:
            return qualifierType.subclass(*args_, **kwargs_)
        else:
            return qualifierType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_step_size(self):
        return self.step_size
    def set_step_size(self, step_size):
        self.step_size = step_size
    def get_step_cost(self):
        return self.step_cost
    def set_step_cost(self, step_cost):
        self.step_cost = step_cost
    def get_included_amount(self):
        return self.included_amount
    def set_included_amount(self, included_amount):
        self.included_amount = included_amount
    def get_max_value(self):
        return self.max_value
    def set_max_value(self, max_value):
        self.max_value = max_value
    def get_included(self):
        return self.included
    def set_included(self, included):
        self.included = included
    def get_percent(self):
        return self.percent
    def set_percent(self, percent):
        self.percent = percent
    def _hasContent(self):
        if (
            self.step_size is not None or
            self.step_cost is not None or
            self.included_amount is not None or
            self.max_value is not None or
            self.included is not None or
            self.percent is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='qualifierType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('qualifierType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'qualifierType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='qualifierType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='qualifierType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='qualifierType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='qualifierType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.step_size is not None:
            namespaceprefix_ = self.step_size_nsprefix_ + ':' if (UseCapturedNS_ and self.step_size_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstep-size>%s</%sstep-size>%s' % (namespaceprefix_ , self.gds_format_decimal(self.step_size, input_name='step-size'), namespaceprefix_ , eol_))
        if self.step_cost is not None:
            namespaceprefix_ = self.step_cost_nsprefix_ + ':' if (UseCapturedNS_ and self.step_cost_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstep-cost>%s</%sstep-cost>%s' % (namespaceprefix_ , self.gds_format_decimal(self.step_cost, input_name='step-cost'), namespaceprefix_ , eol_))
        if self.included_amount is not None:
            namespaceprefix_ = self.included_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.included_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sincluded-amount>%s</%sincluded-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.included_amount, input_name='included-amount'), namespaceprefix_ , eol_))
        if self.max_value is not None:
            namespaceprefix_ = self.max_value_nsprefix_ + ':' if (UseCapturedNS_ and self.max_value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smax-value>%s</%smax-value>%s' % (namespaceprefix_ , self.gds_format_decimal(self.max_value, input_name='max-value'), namespaceprefix_ , eol_))
        if self.included is not None:
            namespaceprefix_ = self.included_nsprefix_ + ':' if (UseCapturedNS_ and self.included_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sincluded>%s</%sincluded>%s' % (namespaceprefix_ , self.gds_format_boolean(self.included, input_name='included'), namespaceprefix_ , eol_))
        if self.percent is not None:
            namespaceprefix_ = self.percent_nsprefix_ + ':' if (UseCapturedNS_ and self.percent_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spercent>%s</%spercent>%s' % (namespaceprefix_ , self.gds_format_decimal(self.percent, input_name='percent'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'step-size' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'step_size')
            fval_ = self.gds_validate_decimal(fval_, node, 'step_size')
            self.step_size = fval_
            self.step_size_nsprefix_ = child_.prefix
        elif nodeName_ == 'step-cost' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'step_cost')
            fval_ = self.gds_validate_decimal(fval_, node, 'step_cost')
            self.step_cost = fval_
            self.step_cost_nsprefix_ = child_.prefix
        elif nodeName_ == 'included-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'included_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'included_amount')
            self.included_amount = fval_
            self.included_amount_nsprefix_ = child_.prefix
        elif nodeName_ == 'max-value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'max_value')
            fval_ = self.gds_validate_decimal(fval_, node, 'max_value')
            self.max_value = fval_
            self.max_value_nsprefix_ = child_.prefix
        elif nodeName_ == 'included':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'included')
            ival_ = self.gds_validate_boolean(ival_, node, 'included')
            self.included = ival_
            self.included_nsprefix_ = child_.prefix
        elif nodeName_ == 'percent' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'percent')
            fval_ = self.gds_validate_decimal(fval_, node, 'percent')
            self.percent = fval_
            self.percent_nsprefix_ = child_.prefix
# end class qualifierType


class adjustmentsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, adjustment=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if adjustment is None:
            self.adjustment = []
        else:
            self.adjustment = adjustment
        self.adjustment_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, adjustmentsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if adjustmentsType.subclass:
            return adjustmentsType.subclass(*args_, **kwargs_)
        else:
            return adjustmentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_adjustment(self):
        return self.adjustment
    def set_adjustment(self, adjustment):
        self.adjustment = adjustment
    def add_adjustment(self, value):
        self.adjustment.append(value)
    def insert_adjustment_at(self, index, value):
        self.adjustment.insert(index, value)
    def replace_adjustment_at(self, index, value):
        self.adjustment[index] = value
    def _hasContent(self):
        if (
            self.adjustment
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='adjustmentsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('adjustmentsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'adjustmentsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='adjustmentsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='adjustmentsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='adjustmentsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='adjustmentsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for adjustment_ in self.adjustment:
            namespaceprefix_ = self.adjustment_nsprefix_ + ':' if (UseCapturedNS_ and self.adjustment_nsprefix_) else ''
            adjustment_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='adjustment', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'adjustment':
            obj_ = adjustmentType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.adjustment.append(obj_)
            obj_.original_tagname_ = 'adjustment'
# end class adjustmentsType


class adjustmentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, adjustment_code=None, adjustment_name=None, adjustment_cost=None, qualifier=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.adjustment_code = adjustment_code
        self.adjustment_code_nsprefix_ = None
        self.adjustment_name = adjustment_name
        self.adjustment_name_nsprefix_ = None
        self.adjustment_cost = adjustment_cost
        self.adjustment_cost_nsprefix_ = None
        self.qualifier = qualifier
        self.qualifier_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, adjustmentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if adjustmentType.subclass:
            return adjustmentType.subclass(*args_, **kwargs_)
        else:
            return adjustmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_adjustment_code(self):
        return self.adjustment_code
    def set_adjustment_code(self, adjustment_code):
        self.adjustment_code = adjustment_code
    def get_adjustment_name(self):
        return self.adjustment_name
    def set_adjustment_name(self, adjustment_name):
        self.adjustment_name = adjustment_name
    def get_adjustment_cost(self):
        return self.adjustment_cost
    def set_adjustment_cost(self, adjustment_cost):
        self.adjustment_cost = adjustment_cost
    def get_qualifier(self):
        return self.qualifier
    def set_qualifier(self, qualifier):
        self.qualifier = qualifier
    def _hasContent(self):
        if (
            self.adjustment_code is not None or
            self.adjustment_name is not None or
            self.adjustment_cost is not None or
            self.qualifier is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='adjustmentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('adjustmentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'adjustmentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='adjustmentType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='adjustmentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='adjustmentType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='adjustmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.adjustment_code is not None:
            namespaceprefix_ = self.adjustment_code_nsprefix_ + ':' if (UseCapturedNS_ and self.adjustment_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadjustment-code>%s</%sadjustment-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.adjustment_code), input_name='adjustment-code')), namespaceprefix_ , eol_))
        if self.adjustment_name is not None:
            namespaceprefix_ = self.adjustment_name_nsprefix_ + ':' if (UseCapturedNS_ and self.adjustment_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadjustment-name>%s</%sadjustment-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.adjustment_name), input_name='adjustment-name')), namespaceprefix_ , eol_))
        if self.adjustment_cost is not None:
            namespaceprefix_ = self.adjustment_cost_nsprefix_ + ':' if (UseCapturedNS_ and self.adjustment_cost_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadjustment-cost>%s</%sadjustment-cost>%s' % (namespaceprefix_ , self.gds_format_decimal(self.adjustment_cost, input_name='adjustment-cost'), namespaceprefix_ , eol_))
        if self.qualifier is not None:
            namespaceprefix_ = self.qualifier_nsprefix_ + ':' if (UseCapturedNS_ and self.qualifier_nsprefix_) else ''
            self.qualifier.export(outfile, level, namespaceprefix_, namespacedef_='', name_='qualifier', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'adjustment-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'adjustment_code')
            value_ = self.gds_validate_string(value_, node, 'adjustment_code')
            self.adjustment_code = value_
            self.adjustment_code_nsprefix_ = child_.prefix
        elif nodeName_ == 'adjustment-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'adjustment_name')
            value_ = self.gds_validate_string(value_, node, 'adjustment_name')
            self.adjustment_name = value_
            self.adjustment_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'adjustment-cost' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'adjustment_cost')
            fval_ = self.gds_validate_decimal(fval_, node, 'adjustment_cost')
            self.adjustment_cost = fval_
            self.adjustment_cost_nsprefix_ = child_.prefix
        elif nodeName_ == 'qualifier':
            obj_ = qualifierType3.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.qualifier = obj_
            obj_.original_tagname_ = 'qualifier'
# end class adjustmentType


class qualifierType3(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, percent=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.percent = percent
        self.percent_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, qualifierType3)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if qualifierType3.subclass:
            return qualifierType3.subclass(*args_, **kwargs_)
        else:
            return qualifierType3(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_percent(self):
        return self.percent
    def set_percent(self, percent):
        self.percent = percent
    def _hasContent(self):
        if (
            self.percent is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='qualifierType3', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('qualifierType3')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'qualifierType3':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='qualifierType3')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='qualifierType3', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='qualifierType3'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='qualifierType3', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.percent is not None:
            namespaceprefix_ = self.percent_nsprefix_ + ':' if (UseCapturedNS_ and self.percent_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spercent>%s</%spercent>%s' % (namespaceprefix_ , self.gds_format_decimal(self.percent, input_name='percent'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'percent' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'percent')
            fval_ = self.gds_validate_decimal(fval_, node, 'percent')
            self.percent = fval_
            self.percent_nsprefix_ = child_.prefix
# end class qualifierType3


class weight_detailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, cubed_weight=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.cubed_weight = cubed_weight
        self.cubed_weight_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, weight_detailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if weight_detailsType.subclass:
            return weight_detailsType.subclass(*args_, **kwargs_)
        else:
            return weight_detailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_cubed_weight(self):
        return self.cubed_weight
    def set_cubed_weight(self, cubed_weight):
        self.cubed_weight = cubed_weight
    def _hasContent(self):
        if (
            self.cubed_weight is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='weight-detailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('weight-detailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'weight-detailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='weight-detailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='weight-detailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='weight-detailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='weight-detailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cubed_weight is not None:
            namespaceprefix_ = self.cubed_weight_nsprefix_ + ':' if (UseCapturedNS_ and self.cubed_weight_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scubed-weight>%s</%scubed-weight>%s' % (namespaceprefix_ , self.gds_format_decimal(self.cubed_weight, input_name='cubed-weight'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'cubed-weight' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'cubed_weight')
            fval_ = self.gds_validate_decimal(fval_, node, 'cubed_weight')
            self.cubed_weight = fval_
            self.cubed_weight_nsprefix_ = child_.prefix
# end class weight_detailsType


class service_standardType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, am_delivery=None, guaranteed_delivery=None, expected_transit_time=None, expected_delivery_date=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.am_delivery = am_delivery
        self.am_delivery_nsprefix_ = None
        self.guaranteed_delivery = guaranteed_delivery
        self.guaranteed_delivery_nsprefix_ = None
        self.expected_transit_time = expected_transit_time
        self.validate_expected_transit_timeType(self.expected_transit_time)
        self.expected_transit_time_nsprefix_ = None
        if isinstance(expected_delivery_date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(expected_delivery_date, '%Y-%m-%d').date()
        else:
            initvalue_ = expected_delivery_date
        self.expected_delivery_date = initvalue_
        self.expected_delivery_date_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, service_standardType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if service_standardType.subclass:
            return service_standardType.subclass(*args_, **kwargs_)
        else:
            return service_standardType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_am_delivery(self):
        return self.am_delivery
    def set_am_delivery(self, am_delivery):
        self.am_delivery = am_delivery
    def get_guaranteed_delivery(self):
        return self.guaranteed_delivery
    def set_guaranteed_delivery(self, guaranteed_delivery):
        self.guaranteed_delivery = guaranteed_delivery
    def get_expected_transit_time(self):
        return self.expected_transit_time
    def set_expected_transit_time(self, expected_transit_time):
        self.expected_transit_time = expected_transit_time
    def get_expected_delivery_date(self):
        return self.expected_delivery_date
    def set_expected_delivery_date(self, expected_delivery_date):
        self.expected_delivery_date = expected_delivery_date
    def validate_expected_transit_timeType(self, value):
        result = True
        # Validate type expected-transit-timeType, a restriction on xsd:integer.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on expected-transit-timeType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 99:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on expected-transit-timeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.am_delivery is not None or
            self.guaranteed_delivery is not None or
            self.expected_transit_time is not None or
            self.expected_delivery_date is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='service-standardType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('service-standardType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'service-standardType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='service-standardType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='service-standardType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='service-standardType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='service-standardType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.am_delivery is not None:
            namespaceprefix_ = self.am_delivery_nsprefix_ + ':' if (UseCapturedNS_ and self.am_delivery_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sam-delivery>%s</%sam-delivery>%s' % (namespaceprefix_ , self.gds_format_boolean(self.am_delivery, input_name='am-delivery'), namespaceprefix_ , eol_))
        if self.guaranteed_delivery is not None:
            namespaceprefix_ = self.guaranteed_delivery_nsprefix_ + ':' if (UseCapturedNS_ and self.guaranteed_delivery_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sguaranteed-delivery>%s</%sguaranteed-delivery>%s' % (namespaceprefix_ , self.gds_format_boolean(self.guaranteed_delivery, input_name='guaranteed-delivery'), namespaceprefix_ , eol_))
        if self.expected_transit_time is not None:
            namespaceprefix_ = self.expected_transit_time_nsprefix_ + ':' if (UseCapturedNS_ and self.expected_transit_time_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexpected-transit-time>%s</%sexpected-transit-time>%s' % (namespaceprefix_ , self.gds_format_integer(self.expected_transit_time, input_name='expected-transit-time'), namespaceprefix_ , eol_))
        if self.expected_delivery_date is not None:
            namespaceprefix_ = self.expected_delivery_date_nsprefix_ + ':' if (UseCapturedNS_ and self.expected_delivery_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexpected-delivery-date>%s</%sexpected-delivery-date>%s' % (namespaceprefix_ , self.gds_format_date(self.expected_delivery_date, input_name='expected-delivery-date'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'am-delivery':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'am_delivery')
            ival_ = self.gds_validate_boolean(ival_, node, 'am_delivery')
            self.am_delivery = ival_
            self.am_delivery_nsprefix_ = child_.prefix
        elif nodeName_ == 'guaranteed-delivery':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'guaranteed_delivery')
            ival_ = self.gds_validate_boolean(ival_, node, 'guaranteed_delivery')
            self.guaranteed_delivery = ival_
            self.guaranteed_delivery_nsprefix_ = child_.prefix
        elif nodeName_ == 'expected-transit-time' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'expected_transit_time')
            ival_ = self.gds_validate_integer(ival_, node, 'expected_transit_time')
            self.expected_transit_time = ival_
            self.expected_transit_time_nsprefix_ = child_.prefix
            # validate type expected-transit-timeType
            self.validate_expected_transit_timeType(self.expected_transit_time)
        elif nodeName_ == 'expected-delivery-date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.expected_delivery_date = dval_
            self.expected_delivery_date_nsprefix_ = child_.prefix
# end class service_standardType


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'mailing_scenario'
        rootClass = mailing_scenario
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'mailing_scenario'
        rootClass = mailing_scenario
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'mailing_scenario'
        rootClass = mailing_scenario
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'mailing_scenario'
        rootClass = mailing_scenario
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from rating import *\n\n')
        sys.stdout.write('import rating as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://www.canadapost.ca/ws/ship/rate-v4': [('PromoCodeType',
                                               './schemas/rating.xsd',
                                               'ST'),
                                              ('IntlPostalCodeType',
                                               './schemas/rating.xsd',
                                               'ST'),
                                              ('TaxType',
                                               './schemas/rating.xsd',
                                               'CT')]}

__all__ = [
    "TaxType",
    "adjustmentType",
    "adjustmentsType",
    "destinationType",
    "dimensionsType",
    "domesticType",
    "internationalType",
    "mailing_scenario",
    "optionType",
    "optionType2",
    "optionsType",
    "optionsType1",
    "parcel_characteristicsType",
    "price_detailsType",
    "price_quoteType",
    "price_quotes",
    "qualifierType",
    "qualifierType3",
    "service_standardType",
    "servicesType",
    "taxesType",
    "united_statesType",
    "weight_detailsType"
]
