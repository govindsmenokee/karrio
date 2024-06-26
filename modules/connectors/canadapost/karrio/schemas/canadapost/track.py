#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Jul 14 15:39:46 2021 by generateDS.py version 2.39.2.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './canadapost_lib/track.py')
#
# Command line arguments:
#   ./schemas/track.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-carriers/.venv/karrio-carriers/bin/generateDS --no-namespace-defs -o "./canadapost_lib/track.py" ./schemas/track.xsd
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


class emptyDate(str, Enum):
    _=''


class tracking_summary(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pin_summary=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if pin_summary is None:
            self.pin_summary = []
        else:
            self.pin_summary = pin_summary
        self.pin_summary_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tracking_summary)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tracking_summary.subclass:
            return tracking_summary.subclass(*args_, **kwargs_)
        else:
            return tracking_summary(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pin_summary(self):
        return self.pin_summary
    def set_pin_summary(self, pin_summary):
        self.pin_summary = pin_summary
    def add_pin_summary(self, value):
        self.pin_summary.append(value)
    def insert_pin_summary_at(self, index, value):
        self.pin_summary.insert(index, value)
    def replace_pin_summary_at(self, index, value):
        self.pin_summary[index] = value
    def _hasContent(self):
        if (
            self.pin_summary
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tracking-summary', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tracking-summary')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tracking-summary':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tracking-summary')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tracking-summary', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tracking-summary'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tracking-summary', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for pin_summary_ in self.pin_summary:
            namespaceprefix_ = self.pin_summary_nsprefix_ + ':' if (UseCapturedNS_ and self.pin_summary_nsprefix_) else ''
            pin_summary_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pin-summary', pretty_print=pretty_print)
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
        if nodeName_ == 'pin-summary':
            obj_ = pin_summary.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pin_summary.append(obj_)
            obj_.original_tagname_ = 'pin-summary'
# end class tracking_summary


class tracking_detail(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pin=None, active_exists=None, archive_exists=None, changed_expected_date=None, destination_postal_id=None, expected_delivery_date=None, changed_expected_delivery_reason=None, mailed_by_customer_number=None, mailed_on_behalf_of_customer_number=None, original_pin=None, service_name=None, service_name_2=None, customer_ref_1=None, customer_ref_2=None, return_pin=None, signature_image_exists=None, suppress_signature=None, delivery_options=None, cod_remit_info=None, significant_events=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.pin = pin
        self.pin_nsprefix_ = None
        self.active_exists = active_exists
        self.active_exists_nsprefix_ = None
        self.archive_exists = archive_exists
        self.archive_exists_nsprefix_ = None
        self.changed_expected_date = changed_expected_date
        self.changed_expected_date_nsprefix_ = None
        self.destination_postal_id = destination_postal_id
        self.destination_postal_id_nsprefix_ = None
        self.expected_delivery_date = expected_delivery_date
        self.validate_emptyDate(self.expected_delivery_date)
        self.expected_delivery_date_nsprefix_ = None
        self.changed_expected_delivery_reason = changed_expected_delivery_reason
        self.changed_expected_delivery_reason_nsprefix_ = None
        self.mailed_by_customer_number = mailed_by_customer_number
        self.mailed_by_customer_number_nsprefix_ = None
        self.mailed_on_behalf_of_customer_number = mailed_on_behalf_of_customer_number
        self.mailed_on_behalf_of_customer_number_nsprefix_ = None
        self.original_pin = original_pin
        self.original_pin_nsprefix_ = None
        self.service_name = service_name
        self.service_name_nsprefix_ = None
        self.service_name_2 = service_name_2
        self.service_name_2_nsprefix_ = None
        self.customer_ref_1 = customer_ref_1
        self.customer_ref_1_nsprefix_ = None
        self.customer_ref_2 = customer_ref_2
        self.customer_ref_2_nsprefix_ = None
        self.return_pin = return_pin
        self.return_pin_nsprefix_ = None
        self.signature_image_exists = signature_image_exists
        self.signature_image_exists_nsprefix_ = None
        self.suppress_signature = suppress_signature
        self.suppress_signature_nsprefix_ = None
        self.delivery_options = delivery_options
        self.delivery_options_nsprefix_ = None
        self.cod_remit_info = cod_remit_info
        self.cod_remit_info_nsprefix_ = None
        self.significant_events = significant_events
        self.significant_events_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tracking_detail)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tracking_detail.subclass:
            return tracking_detail.subclass(*args_, **kwargs_)
        else:
            return tracking_detail(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pin(self):
        return self.pin
    def set_pin(self, pin):
        self.pin = pin
    def get_active_exists(self):
        return self.active_exists
    def set_active_exists(self, active_exists):
        self.active_exists = active_exists
    def get_archive_exists(self):
        return self.archive_exists
    def set_archive_exists(self, archive_exists):
        self.archive_exists = archive_exists
    def get_changed_expected_date(self):
        return self.changed_expected_date
    def set_changed_expected_date(self, changed_expected_date):
        self.changed_expected_date = changed_expected_date
    def get_destination_postal_id(self):
        return self.destination_postal_id
    def set_destination_postal_id(self, destination_postal_id):
        self.destination_postal_id = destination_postal_id
    def get_expected_delivery_date(self):
        return self.expected_delivery_date
    def set_expected_delivery_date(self, expected_delivery_date):
        self.expected_delivery_date = expected_delivery_date
    def get_changed_expected_delivery_reason(self):
        return self.changed_expected_delivery_reason
    def set_changed_expected_delivery_reason(self, changed_expected_delivery_reason):
        self.changed_expected_delivery_reason = changed_expected_delivery_reason
    def get_mailed_by_customer_number(self):
        return self.mailed_by_customer_number
    def set_mailed_by_customer_number(self, mailed_by_customer_number):
        self.mailed_by_customer_number = mailed_by_customer_number
    def get_mailed_on_behalf_of_customer_number(self):
        return self.mailed_on_behalf_of_customer_number
    def set_mailed_on_behalf_of_customer_number(self, mailed_on_behalf_of_customer_number):
        self.mailed_on_behalf_of_customer_number = mailed_on_behalf_of_customer_number
    def get_original_pin(self):
        return self.original_pin
    def set_original_pin(self, original_pin):
        self.original_pin = original_pin
    def get_service_name(self):
        return self.service_name
    def set_service_name(self, service_name):
        self.service_name = service_name
    def get_service_name_2(self):
        return self.service_name_2
    def set_service_name_2(self, service_name_2):
        self.service_name_2 = service_name_2
    def get_customer_ref_1(self):
        return self.customer_ref_1
    def set_customer_ref_1(self, customer_ref_1):
        self.customer_ref_1 = customer_ref_1
    def get_customer_ref_2(self):
        return self.customer_ref_2
    def set_customer_ref_2(self, customer_ref_2):
        self.customer_ref_2 = customer_ref_2
    def get_return_pin(self):
        return self.return_pin
    def set_return_pin(self, return_pin):
        self.return_pin = return_pin
    def get_signature_image_exists(self):
        return self.signature_image_exists
    def set_signature_image_exists(self, signature_image_exists):
        self.signature_image_exists = signature_image_exists
    def get_suppress_signature(self):
        return self.suppress_signature
    def set_suppress_signature(self, suppress_signature):
        self.suppress_signature = suppress_signature
    def get_delivery_options(self):
        return self.delivery_options
    def set_delivery_options(self, delivery_options):
        self.delivery_options = delivery_options
    def get_cod_remit_info(self):
        return self.cod_remit_info
    def set_cod_remit_info(self, cod_remit_info):
        self.cod_remit_info = cod_remit_info
    def get_significant_events(self):
        return self.significant_events
    def set_significant_events(self, significant_events):
        self.significant_events = significant_events
    def validate_emptyDate(self, value):
        result = True
        # Validate type emptyDate, a restriction on xsd:string.
        pass
        return result
    def _hasContent(self):
        if (
            self.pin is not None or
            self.active_exists is not None or
            self.archive_exists is not None or
            self.changed_expected_date is not None or
            self.destination_postal_id is not None or
            self.expected_delivery_date is not None or
            self.changed_expected_delivery_reason is not None or
            self.mailed_by_customer_number is not None or
            self.mailed_on_behalf_of_customer_number is not None or
            self.original_pin is not None or
            self.service_name is not None or
            self.service_name_2 is not None or
            self.customer_ref_1 is not None or
            self.customer_ref_2 is not None or
            self.return_pin is not None or
            self.signature_image_exists is not None or
            self.suppress_signature is not None or
            self.delivery_options is not None or
            self.cod_remit_info is not None or
            self.significant_events is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tracking-detail', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tracking-detail')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tracking-detail':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tracking-detail')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tracking-detail', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tracking-detail'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='tracking-detail', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.pin is not None:
            namespaceprefix_ = self.pin_nsprefix_ + ':' if (UseCapturedNS_ and self.pin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spin>%s</%spin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pin), input_name='pin')), namespaceprefix_ , eol_))
        if self.active_exists is not None:
            namespaceprefix_ = self.active_exists_nsprefix_ + ':' if (UseCapturedNS_ and self.active_exists_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sactive-exists>%s</%sactive-exists>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.active_exists), input_name='active-exists')), namespaceprefix_ , eol_))
        if self.archive_exists is not None:
            namespaceprefix_ = self.archive_exists_nsprefix_ + ':' if (UseCapturedNS_ and self.archive_exists_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sarchive-exists>%s</%sarchive-exists>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.archive_exists), input_name='archive-exists')), namespaceprefix_ , eol_))
        if self.changed_expected_date is not None:
            namespaceprefix_ = self.changed_expected_date_nsprefix_ + ':' if (UseCapturedNS_ and self.changed_expected_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%schanged-expected-date>%s</%schanged-expected-date>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.changed_expected_date), input_name='changed-expected-date')), namespaceprefix_ , eol_))
        if self.destination_postal_id is not None:
            namespaceprefix_ = self.destination_postal_id_nsprefix_ + ':' if (UseCapturedNS_ and self.destination_postal_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdestination-postal-id>%s</%sdestination-postal-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.destination_postal_id), input_name='destination-postal-id')), namespaceprefix_ , eol_))
        if self.expected_delivery_date is not None:
            namespaceprefix_ = self.expected_delivery_date_nsprefix_ + ':' if (UseCapturedNS_ and self.expected_delivery_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexpected-delivery-date>%s</%sexpected-delivery-date>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.expected_delivery_date), input_name='expected-delivery-date')), namespaceprefix_ , eol_))
        if self.changed_expected_delivery_reason is not None:
            namespaceprefix_ = self.changed_expected_delivery_reason_nsprefix_ + ':' if (UseCapturedNS_ and self.changed_expected_delivery_reason_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%schanged-expected-delivery-reason>%s</%schanged-expected-delivery-reason>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.changed_expected_delivery_reason), input_name='changed-expected-delivery-reason')), namespaceprefix_ , eol_))
        if self.mailed_by_customer_number is not None:
            namespaceprefix_ = self.mailed_by_customer_number_nsprefix_ + ':' if (UseCapturedNS_ and self.mailed_by_customer_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smailed-by-customer-number>%s</%smailed-by-customer-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.mailed_by_customer_number), input_name='mailed-by-customer-number')), namespaceprefix_ , eol_))
        if self.mailed_on_behalf_of_customer_number is not None:
            namespaceprefix_ = self.mailed_on_behalf_of_customer_number_nsprefix_ + ':' if (UseCapturedNS_ and self.mailed_on_behalf_of_customer_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smailed-on-behalf-of-customer-number>%s</%smailed-on-behalf-of-customer-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.mailed_on_behalf_of_customer_number), input_name='mailed-on-behalf-of-customer-number')), namespaceprefix_ , eol_))
        if self.original_pin is not None:
            namespaceprefix_ = self.original_pin_nsprefix_ + ':' if (UseCapturedNS_ and self.original_pin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soriginal-pin>%s</%soriginal-pin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.original_pin), input_name='original-pin')), namespaceprefix_ , eol_))
        if self.service_name is not None:
            namespaceprefix_ = self.service_name_nsprefix_ + ':' if (UseCapturedNS_ and self.service_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-name>%s</%sservice-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_name), input_name='service-name')), namespaceprefix_ , eol_))
        if self.service_name_2 is not None:
            namespaceprefix_ = self.service_name_2_nsprefix_ + ':' if (UseCapturedNS_ and self.service_name_2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-name-2>%s</%sservice-name-2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_name_2), input_name='service-name-2')), namespaceprefix_ , eol_))
        if self.customer_ref_1 is not None:
            namespaceprefix_ = self.customer_ref_1_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_ref_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-ref-1>%s</%scustomer-ref-1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_ref_1), input_name='customer-ref-1')), namespaceprefix_ , eol_))
        if self.customer_ref_2 is not None:
            namespaceprefix_ = self.customer_ref_2_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_ref_2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-ref-2>%s</%scustomer-ref-2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_ref_2), input_name='customer-ref-2')), namespaceprefix_ , eol_))
        if self.return_pin is not None:
            namespaceprefix_ = self.return_pin_nsprefix_ + ':' if (UseCapturedNS_ and self.return_pin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreturn-pin>%s</%sreturn-pin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.return_pin), input_name='return-pin')), namespaceprefix_ , eol_))
        if self.signature_image_exists is not None:
            namespaceprefix_ = self.signature_image_exists_nsprefix_ + ':' if (UseCapturedNS_ and self.signature_image_exists_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssignature-image-exists>%s</%ssignature-image-exists>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.signature_image_exists), input_name='signature-image-exists')), namespaceprefix_ , eol_))
        if self.suppress_signature is not None:
            namespaceprefix_ = self.suppress_signature_nsprefix_ + ':' if (UseCapturedNS_ and self.suppress_signature_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssuppress-signature>%s</%ssuppress-signature>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.suppress_signature), input_name='suppress-signature')), namespaceprefix_ , eol_))
        if self.delivery_options is not None:
            namespaceprefix_ = self.delivery_options_nsprefix_ + ':' if (UseCapturedNS_ and self.delivery_options_nsprefix_) else ''
            self.delivery_options.export(outfile, level, namespaceprefix_, namespacedef_='', name_='delivery-options', pretty_print=pretty_print)
        if self.cod_remit_info is not None:
            namespaceprefix_ = self.cod_remit_info_nsprefix_ + ':' if (UseCapturedNS_ and self.cod_remit_info_nsprefix_) else ''
            self.cod_remit_info.export(outfile, level, namespaceprefix_, namespacedef_='', name_='cod-remit-info', pretty_print=pretty_print)
        if self.significant_events is not None:
            namespaceprefix_ = self.significant_events_nsprefix_ + ':' if (UseCapturedNS_ and self.significant_events_nsprefix_) else ''
            self.significant_events.export(outfile, level, namespaceprefix_, namespacedef_='', name_='significant-events', pretty_print=pretty_print)
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
        if nodeName_ == 'pin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pin')
            value_ = self.gds_validate_string(value_, node, 'pin')
            self.pin = value_
            self.pin_nsprefix_ = child_.prefix
        elif nodeName_ == 'active-exists':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'active_exists')
            value_ = self.gds_validate_string(value_, node, 'active_exists')
            self.active_exists = value_
            self.active_exists_nsprefix_ = child_.prefix
        elif nodeName_ == 'archive-exists':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'archive_exists')
            value_ = self.gds_validate_string(value_, node, 'archive_exists')
            self.archive_exists = value_
            self.archive_exists_nsprefix_ = child_.prefix
        elif nodeName_ == 'changed-expected-date':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'changed_expected_date')
            value_ = self.gds_validate_string(value_, node, 'changed_expected_date')
            self.changed_expected_date = value_
            self.changed_expected_date_nsprefix_ = child_.prefix
        elif nodeName_ == 'destination-postal-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'destination_postal_id')
            value_ = self.gds_validate_string(value_, node, 'destination_postal_id')
            self.destination_postal_id = value_
            self.destination_postal_id_nsprefix_ = child_.prefix
        elif nodeName_ == 'expected-delivery-date':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'expected_delivery_date')
            value_ = self.gds_validate_string(value_, node, 'expected_delivery_date')
            self.expected_delivery_date = value_
            self.expected_delivery_date_nsprefix_ = child_.prefix
            # validate type emptyDate
            self.validate_emptyDate(self.expected_delivery_date)
        elif nodeName_ == 'changed-expected-delivery-reason':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'changed_expected_delivery_reason')
            value_ = self.gds_validate_string(value_, node, 'changed_expected_delivery_reason')
            self.changed_expected_delivery_reason = value_
            self.changed_expected_delivery_reason_nsprefix_ = child_.prefix
        elif nodeName_ == 'mailed-by-customer-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mailed_by_customer_number')
            value_ = self.gds_validate_string(value_, node, 'mailed_by_customer_number')
            self.mailed_by_customer_number = value_
            self.mailed_by_customer_number_nsprefix_ = child_.prefix
        elif nodeName_ == 'mailed-on-behalf-of-customer-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mailed_on_behalf_of_customer_number')
            value_ = self.gds_validate_string(value_, node, 'mailed_on_behalf_of_customer_number')
            self.mailed_on_behalf_of_customer_number = value_
            self.mailed_on_behalf_of_customer_number_nsprefix_ = child_.prefix
        elif nodeName_ == 'original-pin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'original_pin')
            value_ = self.gds_validate_string(value_, node, 'original_pin')
            self.original_pin = value_
            self.original_pin_nsprefix_ = child_.prefix
        elif nodeName_ == 'service-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'service_name')
            value_ = self.gds_validate_string(value_, node, 'service_name')
            self.service_name = value_
            self.service_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'service-name-2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'service_name_2')
            value_ = self.gds_validate_string(value_, node, 'service_name_2')
            self.service_name_2 = value_
            self.service_name_2_nsprefix_ = child_.prefix
        elif nodeName_ == 'customer-ref-1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customer_ref_1')
            value_ = self.gds_validate_string(value_, node, 'customer_ref_1')
            self.customer_ref_1 = value_
            self.customer_ref_1_nsprefix_ = child_.prefix
        elif nodeName_ == 'customer-ref-2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customer_ref_2')
            value_ = self.gds_validate_string(value_, node, 'customer_ref_2')
            self.customer_ref_2 = value_
            self.customer_ref_2_nsprefix_ = child_.prefix
        elif nodeName_ == 'return-pin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'return_pin')
            value_ = self.gds_validate_string(value_, node, 'return_pin')
            self.return_pin = value_
            self.return_pin_nsprefix_ = child_.prefix
        elif nodeName_ == 'signature-image-exists':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'signature_image_exists')
            value_ = self.gds_validate_string(value_, node, 'signature_image_exists')
            self.signature_image_exists = value_
            self.signature_image_exists_nsprefix_ = child_.prefix
        elif nodeName_ == 'suppress-signature':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'suppress_signature')
            value_ = self.gds_validate_string(value_, node, 'suppress_signature')
            self.suppress_signature = value_
            self.suppress_signature_nsprefix_ = child_.prefix
        elif nodeName_ == 'delivery-options':
            obj_ = delivery_options.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.delivery_options = obj_
            obj_.original_tagname_ = 'delivery-options'
        elif nodeName_ == 'cod-remit-info':
            obj_ = cod_remit_info.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.cod_remit_info = obj_
            obj_.original_tagname_ = 'cod-remit-info'
        elif nodeName_ == 'significant-events':
            obj_ = significant_events.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.significant_events = obj_
            obj_.original_tagname_ = 'significant-events'
# end class tracking_detail


class signature_image(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, filename=None, image=None, mime_type=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.filename = filename
        self.filename_nsprefix_ = None
        self.image = image
        self.image_nsprefix_ = None
        self.mime_type = mime_type
        self.mime_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, signature_image)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if signature_image.subclass:
            return signature_image.subclass(*args_, **kwargs_)
        else:
            return signature_image(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_filename(self):
        return self.filename
    def set_filename(self, filename):
        self.filename = filename
    def get_image(self):
        return self.image
    def set_image(self, image):
        self.image = image
    def get_mime_type(self):
        return self.mime_type
    def set_mime_type(self, mime_type):
        self.mime_type = mime_type
    def _hasContent(self):
        if (
            self.filename is not None or
            self.image is not None or
            self.mime_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='signature-image', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('signature-image')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'signature-image':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='signature-image')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='signature-image', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='signature-image'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='signature-image', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.filename is not None:
            namespaceprefix_ = self.filename_nsprefix_ + ':' if (UseCapturedNS_ and self.filename_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfilename>%s</%sfilename>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.filename), input_name='filename')), namespaceprefix_ , eol_))
        if self.image is not None:
            namespaceprefix_ = self.image_nsprefix_ + ':' if (UseCapturedNS_ and self.image_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%simage>%s</%simage>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.image), input_name='image')), namespaceprefix_ , eol_))
        if self.mime_type is not None:
            namespaceprefix_ = self.mime_type_nsprefix_ + ':' if (UseCapturedNS_ and self.mime_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smime-type>%s</%smime-type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.mime_type), input_name='mime-type')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'filename':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'filename')
            value_ = self.gds_validate_string(value_, node, 'filename')
            self.filename = value_
            self.filename_nsprefix_ = child_.prefix
        elif nodeName_ == 'image':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'image')
            value_ = self.gds_validate_string(value_, node, 'image')
            self.image = value_
            self.image_nsprefix_ = child_.prefix
        elif nodeName_ == 'mime-type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mime_type')
            value_ = self.gds_validate_string(value_, node, 'mime_type')
            self.mime_type = value_
            self.mime_type_nsprefix_ = child_.prefix
# end class signature_image


class delivery_confirmation_certificate(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, filename=None, image=None, mime_type=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.filename = filename
        self.filename_nsprefix_ = None
        self.image = image
        self.image_nsprefix_ = None
        self.mime_type = mime_type
        self.mime_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, delivery_confirmation_certificate)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if delivery_confirmation_certificate.subclass:
            return delivery_confirmation_certificate.subclass(*args_, **kwargs_)
        else:
            return delivery_confirmation_certificate(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_filename(self):
        return self.filename
    def set_filename(self, filename):
        self.filename = filename
    def get_image(self):
        return self.image
    def set_image(self, image):
        self.image = image
    def get_mime_type(self):
        return self.mime_type
    def set_mime_type(self, mime_type):
        self.mime_type = mime_type
    def _hasContent(self):
        if (
            self.filename is not None or
            self.image is not None or
            self.mime_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='delivery-confirmation-certificate', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('delivery-confirmation-certificate')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'delivery-confirmation-certificate':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='delivery-confirmation-certificate')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='delivery-confirmation-certificate', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='delivery-confirmation-certificate'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='delivery-confirmation-certificate', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.filename is not None:
            namespaceprefix_ = self.filename_nsprefix_ + ':' if (UseCapturedNS_ and self.filename_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfilename>%s</%sfilename>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.filename), input_name='filename')), namespaceprefix_ , eol_))
        if self.image is not None:
            namespaceprefix_ = self.image_nsprefix_ + ':' if (UseCapturedNS_ and self.image_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%simage>%s</%simage>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.image), input_name='image')), namespaceprefix_ , eol_))
        if self.mime_type is not None:
            namespaceprefix_ = self.mime_type_nsprefix_ + ':' if (UseCapturedNS_ and self.mime_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smime-type>%s</%smime-type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.mime_type), input_name='mime-type')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'filename':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'filename')
            value_ = self.gds_validate_string(value_, node, 'filename')
            self.filename = value_
            self.filename_nsprefix_ = child_.prefix
        elif nodeName_ == 'image':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'image')
            value_ = self.gds_validate_string(value_, node, 'image')
            self.image = value_
            self.image_nsprefix_ = child_.prefix
        elif nodeName_ == 'mime-type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mime_type')
            value_ = self.gds_validate_string(value_, node, 'mime_type')
            self.mime_type = value_
            self.mime_type_nsprefix_ = child_.prefix
# end class delivery_confirmation_certificate


class pin_summary(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pin=None, origin_postal_id=None, destination_postal_id=None, destination_province=None, service_name=None, mailed_on_date=None, expected_delivery_date=None, actual_delivery_date=None, delivery_option_completed_ind=None, event_date_time=None, event_description=None, attempted_date=None, customer_ref_1=None, customer_ref_2=None, return_pin=None, event_type=None, event_location=None, signatory_name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.pin = pin
        self.pin_nsprefix_ = None
        self.origin_postal_id = origin_postal_id
        self.origin_postal_id_nsprefix_ = None
        self.destination_postal_id = destination_postal_id
        self.destination_postal_id_nsprefix_ = None
        self.destination_province = destination_province
        self.destination_province_nsprefix_ = None
        self.service_name = service_name
        self.service_name_nsprefix_ = None
        self.mailed_on_date = mailed_on_date
        self.validate_emptyDate(self.mailed_on_date)
        self.mailed_on_date_nsprefix_ = None
        self.expected_delivery_date = expected_delivery_date
        self.validate_emptyDate(self.expected_delivery_date)
        self.expected_delivery_date_nsprefix_ = None
        self.actual_delivery_date = actual_delivery_date
        self.validate_emptyDate(self.actual_delivery_date)
        self.actual_delivery_date_nsprefix_ = None
        self.delivery_option_completed_ind = delivery_option_completed_ind
        self.delivery_option_completed_ind_nsprefix_ = None
        self.event_date_time = event_date_time
        self.event_date_time_nsprefix_ = None
        self.event_description = event_description
        self.event_description_nsprefix_ = None
        self.attempted_date = attempted_date
        self.validate_emptyDate(self.attempted_date)
        self.attempted_date_nsprefix_ = None
        self.customer_ref_1 = customer_ref_1
        self.customer_ref_1_nsprefix_ = None
        self.customer_ref_2 = customer_ref_2
        self.customer_ref_2_nsprefix_ = None
        self.return_pin = return_pin
        self.return_pin_nsprefix_ = None
        self.event_type = event_type
        self.event_type_nsprefix_ = None
        self.event_location = event_location
        self.event_location_nsprefix_ = None
        self.signatory_name = signatory_name
        self.signatory_name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, pin_summary)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if pin_summary.subclass:
            return pin_summary.subclass(*args_, **kwargs_)
        else:
            return pin_summary(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pin(self):
        return self.pin
    def set_pin(self, pin):
        self.pin = pin
    def get_origin_postal_id(self):
        return self.origin_postal_id
    def set_origin_postal_id(self, origin_postal_id):
        self.origin_postal_id = origin_postal_id
    def get_destination_postal_id(self):
        return self.destination_postal_id
    def set_destination_postal_id(self, destination_postal_id):
        self.destination_postal_id = destination_postal_id
    def get_destination_province(self):
        return self.destination_province
    def set_destination_province(self, destination_province):
        self.destination_province = destination_province
    def get_service_name(self):
        return self.service_name
    def set_service_name(self, service_name):
        self.service_name = service_name
    def get_mailed_on_date(self):
        return self.mailed_on_date
    def set_mailed_on_date(self, mailed_on_date):
        self.mailed_on_date = mailed_on_date
    def get_expected_delivery_date(self):
        return self.expected_delivery_date
    def set_expected_delivery_date(self, expected_delivery_date):
        self.expected_delivery_date = expected_delivery_date
    def get_actual_delivery_date(self):
        return self.actual_delivery_date
    def set_actual_delivery_date(self, actual_delivery_date):
        self.actual_delivery_date = actual_delivery_date
    def get_delivery_option_completed_ind(self):
        return self.delivery_option_completed_ind
    def set_delivery_option_completed_ind(self, delivery_option_completed_ind):
        self.delivery_option_completed_ind = delivery_option_completed_ind
    def get_event_date_time(self):
        return self.event_date_time
    def set_event_date_time(self, event_date_time):
        self.event_date_time = event_date_time
    def get_event_description(self):
        return self.event_description
    def set_event_description(self, event_description):
        self.event_description = event_description
    def get_attempted_date(self):
        return self.attempted_date
    def set_attempted_date(self, attempted_date):
        self.attempted_date = attempted_date
    def get_customer_ref_1(self):
        return self.customer_ref_1
    def set_customer_ref_1(self, customer_ref_1):
        self.customer_ref_1 = customer_ref_1
    def get_customer_ref_2(self):
        return self.customer_ref_2
    def set_customer_ref_2(self, customer_ref_2):
        self.customer_ref_2 = customer_ref_2
    def get_return_pin(self):
        return self.return_pin
    def set_return_pin(self, return_pin):
        self.return_pin = return_pin
    def get_event_type(self):
        return self.event_type
    def set_event_type(self, event_type):
        self.event_type = event_type
    def get_event_location(self):
        return self.event_location
    def set_event_location(self, event_location):
        self.event_location = event_location
    def get_signatory_name(self):
        return self.signatory_name
    def set_signatory_name(self, signatory_name):
        self.signatory_name = signatory_name
    def validate_emptyDate(self, value):
        result = True
        # Validate type emptyDate, a restriction on xsd:string.
        pass
        return result
    def _hasContent(self):
        if (
            self.pin is not None or
            self.origin_postal_id is not None or
            self.destination_postal_id is not None or
            self.destination_province is not None or
            self.service_name is not None or
            self.mailed_on_date is not None or
            self.expected_delivery_date is not None or
            self.actual_delivery_date is not None or
            self.delivery_option_completed_ind is not None or
            self.event_date_time is not None or
            self.event_description is not None or
            self.attempted_date is not None or
            self.customer_ref_1 is not None or
            self.customer_ref_2 is not None or
            self.return_pin is not None or
            self.event_type is not None or
            self.event_location is not None or
            self.signatory_name is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='pin-summary', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('pin-summary')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'pin-summary':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='pin-summary')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='pin-summary', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='pin-summary'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='pin-summary', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.pin is not None:
            namespaceprefix_ = self.pin_nsprefix_ + ':' if (UseCapturedNS_ and self.pin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spin>%s</%spin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pin), input_name='pin')), namespaceprefix_ , eol_))
        if self.origin_postal_id is not None:
            namespaceprefix_ = self.origin_postal_id_nsprefix_ + ':' if (UseCapturedNS_ and self.origin_postal_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sorigin-postal-id>%s</%sorigin-postal-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.origin_postal_id), input_name='origin-postal-id')), namespaceprefix_ , eol_))
        if self.destination_postal_id is not None:
            namespaceprefix_ = self.destination_postal_id_nsprefix_ + ':' if (UseCapturedNS_ and self.destination_postal_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdestination-postal-id>%s</%sdestination-postal-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.destination_postal_id), input_name='destination-postal-id')), namespaceprefix_ , eol_))
        if self.destination_province is not None:
            namespaceprefix_ = self.destination_province_nsprefix_ + ':' if (UseCapturedNS_ and self.destination_province_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdestination-province>%s</%sdestination-province>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.destination_province), input_name='destination-province')), namespaceprefix_ , eol_))
        if self.service_name is not None:
            namespaceprefix_ = self.service_name_nsprefix_ + ':' if (UseCapturedNS_ and self.service_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-name>%s</%sservice-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_name), input_name='service-name')), namespaceprefix_ , eol_))
        if self.mailed_on_date is not None:
            namespaceprefix_ = self.mailed_on_date_nsprefix_ + ':' if (UseCapturedNS_ and self.mailed_on_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smailed-on-date>%s</%smailed-on-date>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.mailed_on_date), input_name='mailed-on-date')), namespaceprefix_ , eol_))
        if self.expected_delivery_date is not None:
            namespaceprefix_ = self.expected_delivery_date_nsprefix_ + ':' if (UseCapturedNS_ and self.expected_delivery_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexpected-delivery-date>%s</%sexpected-delivery-date>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.expected_delivery_date), input_name='expected-delivery-date')), namespaceprefix_ , eol_))
        if self.actual_delivery_date is not None:
            namespaceprefix_ = self.actual_delivery_date_nsprefix_ + ':' if (UseCapturedNS_ and self.actual_delivery_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sactual-delivery-date>%s</%sactual-delivery-date>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.actual_delivery_date), input_name='actual-delivery-date')), namespaceprefix_ , eol_))
        if self.delivery_option_completed_ind is not None:
            namespaceprefix_ = self.delivery_option_completed_ind_nsprefix_ + ':' if (UseCapturedNS_ and self.delivery_option_completed_ind_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdelivery-option-completed-ind>%s</%sdelivery-option-completed-ind>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.delivery_option_completed_ind), input_name='delivery-option-completed-ind')), namespaceprefix_ , eol_))
        if self.event_date_time is not None:
            namespaceprefix_ = self.event_date_time_nsprefix_ + ':' if (UseCapturedNS_ and self.event_date_time_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-date-time>%s</%sevent-date-time>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_date_time), input_name='event-date-time')), namespaceprefix_ , eol_))
        if self.event_description is not None:
            namespaceprefix_ = self.event_description_nsprefix_ + ':' if (UseCapturedNS_ and self.event_description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-description>%s</%sevent-description>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_description), input_name='event-description')), namespaceprefix_ , eol_))
        if self.attempted_date is not None:
            namespaceprefix_ = self.attempted_date_nsprefix_ + ':' if (UseCapturedNS_ and self.attempted_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sattempted-date>%s</%sattempted-date>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.attempted_date), input_name='attempted-date')), namespaceprefix_ , eol_))
        if self.customer_ref_1 is not None:
            namespaceprefix_ = self.customer_ref_1_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_ref_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-ref-1>%s</%scustomer-ref-1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_ref_1), input_name='customer-ref-1')), namespaceprefix_ , eol_))
        if self.customer_ref_2 is not None:
            namespaceprefix_ = self.customer_ref_2_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_ref_2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-ref-2>%s</%scustomer-ref-2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_ref_2), input_name='customer-ref-2')), namespaceprefix_ , eol_))
        if self.return_pin is not None:
            namespaceprefix_ = self.return_pin_nsprefix_ + ':' if (UseCapturedNS_ and self.return_pin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreturn-pin>%s</%sreturn-pin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.return_pin), input_name='return-pin')), namespaceprefix_ , eol_))
        if self.event_type is not None:
            namespaceprefix_ = self.event_type_nsprefix_ + ':' if (UseCapturedNS_ and self.event_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-type>%s</%sevent-type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_type), input_name='event-type')), namespaceprefix_ , eol_))
        if self.event_location is not None:
            namespaceprefix_ = self.event_location_nsprefix_ + ':' if (UseCapturedNS_ and self.event_location_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-location>%s</%sevent-location>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_location), input_name='event-location')), namespaceprefix_ , eol_))
        if self.signatory_name is not None:
            namespaceprefix_ = self.signatory_name_nsprefix_ + ':' if (UseCapturedNS_ and self.signatory_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssignatory-name>%s</%ssignatory-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.signatory_name), input_name='signatory-name')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'pin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pin')
            value_ = self.gds_validate_string(value_, node, 'pin')
            self.pin = value_
            self.pin_nsprefix_ = child_.prefix
        elif nodeName_ == 'origin-postal-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'origin_postal_id')
            value_ = self.gds_validate_string(value_, node, 'origin_postal_id')
            self.origin_postal_id = value_
            self.origin_postal_id_nsprefix_ = child_.prefix
        elif nodeName_ == 'destination-postal-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'destination_postal_id')
            value_ = self.gds_validate_string(value_, node, 'destination_postal_id')
            self.destination_postal_id = value_
            self.destination_postal_id_nsprefix_ = child_.prefix
        elif nodeName_ == 'destination-province':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'destination_province')
            value_ = self.gds_validate_string(value_, node, 'destination_province')
            self.destination_province = value_
            self.destination_province_nsprefix_ = child_.prefix
        elif nodeName_ == 'service-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'service_name')
            value_ = self.gds_validate_string(value_, node, 'service_name')
            self.service_name = value_
            self.service_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'mailed-on-date':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mailed_on_date')
            value_ = self.gds_validate_string(value_, node, 'mailed_on_date')
            self.mailed_on_date = value_
            self.mailed_on_date_nsprefix_ = child_.prefix
            # validate type emptyDate
            self.validate_emptyDate(self.mailed_on_date)
        elif nodeName_ == 'expected-delivery-date':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'expected_delivery_date')
            value_ = self.gds_validate_string(value_, node, 'expected_delivery_date')
            self.expected_delivery_date = value_
            self.expected_delivery_date_nsprefix_ = child_.prefix
            # validate type emptyDate
            self.validate_emptyDate(self.expected_delivery_date)
        elif nodeName_ == 'actual-delivery-date':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'actual_delivery_date')
            value_ = self.gds_validate_string(value_, node, 'actual_delivery_date')
            self.actual_delivery_date = value_
            self.actual_delivery_date_nsprefix_ = child_.prefix
            # validate type emptyDate
            self.validate_emptyDate(self.actual_delivery_date)
        elif nodeName_ == 'delivery-option-completed-ind':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'delivery_option_completed_ind')
            value_ = self.gds_validate_string(value_, node, 'delivery_option_completed_ind')
            self.delivery_option_completed_ind = value_
            self.delivery_option_completed_ind_nsprefix_ = child_.prefix
        elif nodeName_ == 'event-date-time':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_date_time')
            value_ = self.gds_validate_string(value_, node, 'event_date_time')
            self.event_date_time = value_
            self.event_date_time_nsprefix_ = child_.prefix
        elif nodeName_ == 'event-description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_description')
            value_ = self.gds_validate_string(value_, node, 'event_description')
            self.event_description = value_
            self.event_description_nsprefix_ = child_.prefix
        elif nodeName_ == 'attempted-date':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'attempted_date')
            value_ = self.gds_validate_string(value_, node, 'attempted_date')
            self.attempted_date = value_
            self.attempted_date_nsprefix_ = child_.prefix
            # validate type emptyDate
            self.validate_emptyDate(self.attempted_date)
        elif nodeName_ == 'customer-ref-1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customer_ref_1')
            value_ = self.gds_validate_string(value_, node, 'customer_ref_1')
            self.customer_ref_1 = value_
            self.customer_ref_1_nsprefix_ = child_.prefix
        elif nodeName_ == 'customer-ref-2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customer_ref_2')
            value_ = self.gds_validate_string(value_, node, 'customer_ref_2')
            self.customer_ref_2 = value_
            self.customer_ref_2_nsprefix_ = child_.prefix
        elif nodeName_ == 'return-pin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'return_pin')
            value_ = self.gds_validate_string(value_, node, 'return_pin')
            self.return_pin = value_
            self.return_pin_nsprefix_ = child_.prefix
        elif nodeName_ == 'event-type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_type')
            value_ = self.gds_validate_string(value_, node, 'event_type')
            self.event_type = value_
            self.event_type_nsprefix_ = child_.prefix
        elif nodeName_ == 'event-location':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_location')
            value_ = self.gds_validate_string(value_, node, 'event_location')
            self.event_location = value_
            self.event_location_nsprefix_ = child_.prefix
        elif nodeName_ == 'signatory-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'signatory_name')
            value_ = self.gds_validate_string(value_, node, 'signatory_name')
            self.signatory_name = value_
            self.signatory_name_nsprefix_ = child_.prefix
# end class pin_summary


class delivery_options(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, delivery_options)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if delivery_options.subclass:
            return delivery_options.subclass(*args_, **kwargs_)
        else:
            return delivery_options(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def _hasContent(self):
        if (
            self.item
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='delivery-options', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('delivery-options')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'delivery-options':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='delivery-options')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='delivery-options', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='delivery-options'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='delivery-options', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for item_ in self.item:
            namespaceprefix_ = self.item_nsprefix_ + ':' if (UseCapturedNS_ and self.item_nsprefix_) else ''
            item_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='item', pretty_print=pretty_print)
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
        if nodeName_ == 'item':
            obj_ = itemType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class delivery_options


class significant_events(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, occurrence=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if occurrence is None:
            self.occurrence = []
        else:
            self.occurrence = occurrence
        self.occurrence_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, significant_events)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if significant_events.subclass:
            return significant_events.subclass(*args_, **kwargs_)
        else:
            return significant_events(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_occurrence(self):
        return self.occurrence
    def set_occurrence(self, occurrence):
        self.occurrence = occurrence
    def add_occurrence(self, value):
        self.occurrence.append(value)
    def insert_occurrence_at(self, index, value):
        self.occurrence.insert(index, value)
    def replace_occurrence_at(self, index, value):
        self.occurrence[index] = value
    def _hasContent(self):
        if (
            self.occurrence
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='significant-events', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('significant-events')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'significant-events':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='significant-events')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='significant-events', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='significant-events'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='significant-events', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for occurrence_ in self.occurrence:
            namespaceprefix_ = self.occurrence_nsprefix_ + ':' if (UseCapturedNS_ and self.occurrence_nsprefix_) else ''
            occurrence_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='occurrence', pretty_print=pretty_print)
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
        if nodeName_ == 'occurrence':
            obj_ = occurrenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.occurrence.append(obj_)
            obj_.original_tagname_ = 'occurrence'
# end class significant_events


class cod_remit_info(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pin=None, type_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.pin = pin
        self.pin_nsprefix_ = None
        self.type_ = type_
        self.type__nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, cod_remit_info)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if cod_remit_info.subclass:
            return cod_remit_info.subclass(*args_, **kwargs_)
        else:
            return cod_remit_info(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pin(self):
        return self.pin
    def set_pin(self, pin):
        self.pin = pin
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def _hasContent(self):
        if (
            self.pin is not None or
            self.type_ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='cod-remit-info', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('cod-remit-info')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'cod-remit-info':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='cod-remit-info')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='cod-remit-info', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='cod-remit-info'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='cod-remit-info', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.pin is not None:
            namespaceprefix_ = self.pin_nsprefix_ + ':' if (UseCapturedNS_ and self.pin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spin>%s</%spin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pin), input_name='pin')), namespaceprefix_ , eol_))
        if self.type_ is not None:
            namespaceprefix_ = self.type__nsprefix_ + ':' if (UseCapturedNS_ and self.type__nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stype>%s</%stype>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.type_), input_name='type')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'pin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pin')
            value_ = self.gds_validate_string(value_, node, 'pin')
            self.pin = value_
            self.pin_nsprefix_ = child_.prefix
        elif nodeName_ == 'type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'type')
            value_ = self.gds_validate_string(value_, node, 'type')
            self.type_ = value_
            self.type_nsprefix_ = child_.prefix
# end class cod_remit_info


class itemType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, delivery_option=None, delivery_option_description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.delivery_option = delivery_option
        self.delivery_option_nsprefix_ = None
        self.delivery_option_description = delivery_option_description
        self.delivery_option_description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType.subclass:
            return itemType.subclass(*args_, **kwargs_)
        else:
            return itemType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_delivery_option(self):
        return self.delivery_option
    def set_delivery_option(self, delivery_option):
        self.delivery_option = delivery_option
    def get_delivery_option_description(self):
        return self.delivery_option_description
    def set_delivery_option_description(self, delivery_option_description):
        self.delivery_option_description = delivery_option_description
    def _hasContent(self):
        if (
            self.delivery_option is not None or
            self.delivery_option_description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='itemType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('itemType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'itemType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='itemType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='itemType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='itemType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='itemType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.delivery_option is not None:
            namespaceprefix_ = self.delivery_option_nsprefix_ + ':' if (UseCapturedNS_ and self.delivery_option_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdelivery-option>%s</%sdelivery-option>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.delivery_option), input_name='delivery-option')), namespaceprefix_ , eol_))
        if self.delivery_option_description is not None:
            namespaceprefix_ = self.delivery_option_description_nsprefix_ + ':' if (UseCapturedNS_ and self.delivery_option_description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdelivery-option-description>%s</%sdelivery-option-description>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.delivery_option_description), input_name='delivery-option-description')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'delivery-option':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'delivery_option')
            value_ = self.gds_validate_string(value_, node, 'delivery_option')
            self.delivery_option = value_
            self.delivery_option_nsprefix_ = child_.prefix
        elif nodeName_ == 'delivery-option-description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'delivery_option_description')
            value_ = self.gds_validate_string(value_, node, 'delivery_option_description')
            self.delivery_option_description = value_
            self.delivery_option_description_nsprefix_ = child_.prefix
# end class itemType


class occurrenceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, event_identifier=None, event_date=None, event_time=None, event_time_zone=None, event_description=None, signatory_name=None, event_site=None, event_province=None, event_retail_location_id=None, event_retail_name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.event_identifier = event_identifier
        self.event_identifier_nsprefix_ = None
        self.event_date = event_date
        self.event_date_nsprefix_ = None
        self.event_time = event_time
        self.event_time_nsprefix_ = None
        self.event_time_zone = event_time_zone
        self.event_time_zone_nsprefix_ = None
        self.event_description = event_description
        self.event_description_nsprefix_ = None
        self.signatory_name = signatory_name
        self.signatory_name_nsprefix_ = None
        self.event_site = event_site
        self.event_site_nsprefix_ = None
        self.event_province = event_province
        self.event_province_nsprefix_ = None
        self.event_retail_location_id = event_retail_location_id
        self.event_retail_location_id_nsprefix_ = None
        self.event_retail_name = event_retail_name
        self.event_retail_name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, occurrenceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if occurrenceType.subclass:
            return occurrenceType.subclass(*args_, **kwargs_)
        else:
            return occurrenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_event_identifier(self):
        return self.event_identifier
    def set_event_identifier(self, event_identifier):
        self.event_identifier = event_identifier
    def get_event_date(self):
        return self.event_date
    def set_event_date(self, event_date):
        self.event_date = event_date
    def get_event_time(self):
        return self.event_time
    def set_event_time(self, event_time):
        self.event_time = event_time
    def get_event_time_zone(self):
        return self.event_time_zone
    def set_event_time_zone(self, event_time_zone):
        self.event_time_zone = event_time_zone
    def get_event_description(self):
        return self.event_description
    def set_event_description(self, event_description):
        self.event_description = event_description
    def get_signatory_name(self):
        return self.signatory_name
    def set_signatory_name(self, signatory_name):
        self.signatory_name = signatory_name
    def get_event_site(self):
        return self.event_site
    def set_event_site(self, event_site):
        self.event_site = event_site
    def get_event_province(self):
        return self.event_province
    def set_event_province(self, event_province):
        self.event_province = event_province
    def get_event_retail_location_id(self):
        return self.event_retail_location_id
    def set_event_retail_location_id(self, event_retail_location_id):
        self.event_retail_location_id = event_retail_location_id
    def get_event_retail_name(self):
        return self.event_retail_name
    def set_event_retail_name(self, event_retail_name):
        self.event_retail_name = event_retail_name
    def _hasContent(self):
        if (
            self.event_identifier is not None or
            self.event_date is not None or
            self.event_time is not None or
            self.event_time_zone is not None or
            self.event_description is not None or
            self.signatory_name is not None or
            self.event_site is not None or
            self.event_province is not None or
            self.event_retail_location_id is not None or
            self.event_retail_name is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='occurrenceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('occurrenceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'occurrenceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='occurrenceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='occurrenceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='occurrenceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='occurrenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.event_identifier is not None:
            namespaceprefix_ = self.event_identifier_nsprefix_ + ':' if (UseCapturedNS_ and self.event_identifier_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-identifier>%s</%sevent-identifier>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_identifier), input_name='event-identifier')), namespaceprefix_ , eol_))
        if self.event_date is not None:
            namespaceprefix_ = self.event_date_nsprefix_ + ':' if (UseCapturedNS_ and self.event_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-date>%s</%sevent-date>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_date), input_name='event-date')), namespaceprefix_ , eol_))
        if self.event_time is not None:
            namespaceprefix_ = self.event_time_nsprefix_ + ':' if (UseCapturedNS_ and self.event_time_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-time>%s</%sevent-time>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_time), input_name='event-time')), namespaceprefix_ , eol_))
        if self.event_time_zone is not None:
            namespaceprefix_ = self.event_time_zone_nsprefix_ + ':' if (UseCapturedNS_ and self.event_time_zone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-time-zone>%s</%sevent-time-zone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_time_zone), input_name='event-time-zone')), namespaceprefix_ , eol_))
        if self.event_description is not None:
            namespaceprefix_ = self.event_description_nsprefix_ + ':' if (UseCapturedNS_ and self.event_description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-description>%s</%sevent-description>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_description), input_name='event-description')), namespaceprefix_ , eol_))
        if self.signatory_name is not None:
            namespaceprefix_ = self.signatory_name_nsprefix_ + ':' if (UseCapturedNS_ and self.signatory_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssignatory-name>%s</%ssignatory-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.signatory_name), input_name='signatory-name')), namespaceprefix_ , eol_))
        if self.event_site is not None:
            namespaceprefix_ = self.event_site_nsprefix_ + ':' if (UseCapturedNS_ and self.event_site_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-site>%s</%sevent-site>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_site), input_name='event-site')), namespaceprefix_ , eol_))
        if self.event_province is not None:
            namespaceprefix_ = self.event_province_nsprefix_ + ':' if (UseCapturedNS_ and self.event_province_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-province>%s</%sevent-province>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_province), input_name='event-province')), namespaceprefix_ , eol_))
        if self.event_retail_location_id is not None:
            namespaceprefix_ = self.event_retail_location_id_nsprefix_ + ':' if (UseCapturedNS_ and self.event_retail_location_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-retail-location-id>%s</%sevent-retail-location-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_retail_location_id), input_name='event-retail-location-id')), namespaceprefix_ , eol_))
        if self.event_retail_name is not None:
            namespaceprefix_ = self.event_retail_name_nsprefix_ + ':' if (UseCapturedNS_ and self.event_retail_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sevent-retail-name>%s</%sevent-retail-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.event_retail_name), input_name='event-retail-name')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'event-identifier':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_identifier')
            value_ = self.gds_validate_string(value_, node, 'event_identifier')
            self.event_identifier = value_
            self.event_identifier_nsprefix_ = child_.prefix
        elif nodeName_ == 'event-date':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_date')
            value_ = self.gds_validate_string(value_, node, 'event_date')
            self.event_date = value_
            self.event_date_nsprefix_ = child_.prefix
        elif nodeName_ == 'event-time':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_time')
            value_ = self.gds_validate_string(value_, node, 'event_time')
            self.event_time = value_
            self.event_time_nsprefix_ = child_.prefix
        elif nodeName_ == 'event-time-zone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_time_zone')
            value_ = self.gds_validate_string(value_, node, 'event_time_zone')
            self.event_time_zone = value_
            self.event_time_zone_nsprefix_ = child_.prefix
        elif nodeName_ == 'event-description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_description')
            value_ = self.gds_validate_string(value_, node, 'event_description')
            self.event_description = value_
            self.event_description_nsprefix_ = child_.prefix
        elif nodeName_ == 'signatory-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'signatory_name')
            value_ = self.gds_validate_string(value_, node, 'signatory_name')
            self.signatory_name = value_
            self.signatory_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'event-site':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_site')
            value_ = self.gds_validate_string(value_, node, 'event_site')
            self.event_site = value_
            self.event_site_nsprefix_ = child_.prefix
        elif nodeName_ == 'event-province':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_province')
            value_ = self.gds_validate_string(value_, node, 'event_province')
            self.event_province = value_
            self.event_province_nsprefix_ = child_.prefix
        elif nodeName_ == 'event-retail-location-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_retail_location_id')
            value_ = self.gds_validate_string(value_, node, 'event_retail_location_id')
            self.event_retail_location_id = value_
            self.event_retail_location_id_nsprefix_ = child_.prefix
        elif nodeName_ == 'event-retail-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'event_retail_name')
            value_ = self.gds_validate_string(value_, node, 'event_retail_name')
            self.event_retail_name = value_
            self.event_retail_name_nsprefix_ = child_.prefix
# end class occurrenceType


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
        rootTag = 'tracking_summary'
        rootClass = tracking_summary
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
        rootTag = 'tracking_summary'
        rootClass = tracking_summary
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
        rootTag = 'tracking_summary'
        rootClass = tracking_summary
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
        rootTag = 'tracking_summary'
        rootClass = tracking_summary
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from track import *\n\n')
        sys.stdout.write('import track as model_\n\n')
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
NamespaceToDefMappings_ = {'http://www.canadapost.ca/ws/track': [('emptyDate',
                                        './schemas/track.xsd',
                                        'ST'),
                                       ('pin_summary',
                                        './schemas/track.xsd',
                                        'CT'),
                                       ('delivery_options',
                                        './schemas/track.xsd',
                                        'CT'),
                                       ('significant_events',
                                        './schemas/track.xsd',
                                        'CT'),
                                       ('cod_remit_info',
                                        './schemas/track.xsd',
                                        'CT')]}

__all__ = [
    "cod_remit_info",
    "delivery_confirmation_certificate",
    "delivery_options",
    "itemType",
    "occurrenceType",
    "pin_summary",
    "signature_image",
    "significant_events",
    "tracking_detail",
    "tracking_summary"
]
