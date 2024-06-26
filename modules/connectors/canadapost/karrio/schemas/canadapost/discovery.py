#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Jul 14 15:39:44 2021 by generateDS.py version 2.39.2.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './canadapost_lib/discovery.py')
#
# Command line arguments:
#   ./schemas/discovery.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-carriers/.venv/karrio-carriers/bin/generateDS --no-namespace-defs -o "./canadapost_lib/discovery.py" ./schemas/discovery.xsd
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


class RelType(str, Enum):
    SERVICE='service'
    OPTION='option'


class services(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if service is None:
            self.service = []
        else:
            self.service = service
        self.service_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, services)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if services.subclass:
            return services.subclass(*args_, **kwargs_)
        else:
            return services(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_service(self):
        return self.service
    def set_service(self, service):
        self.service = service
    def add_service(self, value):
        self.service.append(value)
    def insert_service_at(self, index, value):
        self.service.insert(index, value)
    def replace_service_at(self, index, value):
        self.service[index] = value
    def _hasContent(self):
        if (
            self.service
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='services', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('services')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'services':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='services')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='services', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='services'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='services', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for service_ in self.service:
            namespaceprefix_ = self.service_nsprefix_ + ':' if (UseCapturedNS_ and self.service_nsprefix_) else ''
            service_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='service', pretty_print=pretty_print)
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
        if nodeName_ == 'service':
            obj_ = serviceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.service.append(obj_)
            obj_.original_tagname_ = 'service'
# end class services


class option(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, option_code=None, option_name=None, option_class=None, prints_on_label=None, qualifier_required=None, conflicting_options=None, prerequisite_options=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.option_code = option_code
        self.option_code_nsprefix_ = None
        self.option_name = option_name
        self.option_name_nsprefix_ = None
        self.option_class = option_class
        self.option_class_nsprefix_ = None
        self.prints_on_label = prints_on_label
        self.prints_on_label_nsprefix_ = None
        self.qualifier_required = qualifier_required
        self.qualifier_required_nsprefix_ = None
        self.conflicting_options = conflicting_options
        self.conflicting_options_nsprefix_ = None
        self.prerequisite_options = prerequisite_options
        self.prerequisite_options_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, option)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if option.subclass:
            return option.subclass(*args_, **kwargs_)
        else:
            return option(*args_, **kwargs_)
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
    def get_option_class(self):
        return self.option_class
    def set_option_class(self, option_class):
        self.option_class = option_class
    def get_prints_on_label(self):
        return self.prints_on_label
    def set_prints_on_label(self, prints_on_label):
        self.prints_on_label = prints_on_label
    def get_qualifier_required(self):
        return self.qualifier_required
    def set_qualifier_required(self, qualifier_required):
        self.qualifier_required = qualifier_required
    def get_conflicting_options(self):
        return self.conflicting_options
    def set_conflicting_options(self, conflicting_options):
        self.conflicting_options = conflicting_options
    def get_prerequisite_options(self):
        return self.prerequisite_options
    def set_prerequisite_options(self, prerequisite_options):
        self.prerequisite_options = prerequisite_options
    def _hasContent(self):
        if (
            self.option_code is not None or
            self.option_name is not None or
            self.option_class is not None or
            self.prints_on_label is not None or
            self.qualifier_required is not None or
            self.conflicting_options is not None or
            self.prerequisite_options is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='option', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('option')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'option':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='option')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='option', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='option'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='option', fromsubclass_=False, pretty_print=True):
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
        if self.option_class is not None:
            namespaceprefix_ = self.option_class_nsprefix_ + ':' if (UseCapturedNS_ and self.option_class_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-class>%s</%soption-class>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.option_class), input_name='option-class')), namespaceprefix_ , eol_))
        if self.prints_on_label is not None:
            namespaceprefix_ = self.prints_on_label_nsprefix_ + ':' if (UseCapturedNS_ and self.prints_on_label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprints-on-label>%s</%sprints-on-label>%s' % (namespaceprefix_ , self.gds_format_boolean(self.prints_on_label, input_name='prints-on-label'), namespaceprefix_ , eol_))
        if self.qualifier_required is not None:
            namespaceprefix_ = self.qualifier_required_nsprefix_ + ':' if (UseCapturedNS_ and self.qualifier_required_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%squalifier-required>%s</%squalifier-required>%s' % (namespaceprefix_ , self.gds_format_boolean(self.qualifier_required, input_name='qualifier-required'), namespaceprefix_ , eol_))
        if self.conflicting_options is not None:
            namespaceprefix_ = self.conflicting_options_nsprefix_ + ':' if (UseCapturedNS_ and self.conflicting_options_nsprefix_) else ''
            self.conflicting_options.export(outfile, level, namespaceprefix_, namespacedef_='', name_='conflicting-options', pretty_print=pretty_print)
        if self.prerequisite_options is not None:
            namespaceprefix_ = self.prerequisite_options_nsprefix_ + ':' if (UseCapturedNS_ and self.prerequisite_options_nsprefix_) else ''
            self.prerequisite_options.export(outfile, level, namespaceprefix_, namespacedef_='', name_='prerequisite-options', pretty_print=pretty_print)
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
        elif nodeName_ == 'option-class':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'option_class')
            value_ = self.gds_validate_string(value_, node, 'option_class')
            self.option_class = value_
            self.option_class_nsprefix_ = child_.prefix
        elif nodeName_ == 'prints-on-label':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'prints_on_label')
            ival_ = self.gds_validate_boolean(ival_, node, 'prints_on_label')
            self.prints_on_label = ival_
            self.prints_on_label_nsprefix_ = child_.prefix
        elif nodeName_ == 'qualifier-required':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'qualifier_required')
            ival_ = self.gds_validate_boolean(ival_, node, 'qualifier_required')
            self.qualifier_required = ival_
            self.qualifier_required_nsprefix_ = child_.prefix
        elif nodeName_ == 'conflicting-options':
            obj_ = conflicting_optionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.conflicting_options = obj_
            obj_.original_tagname_ = 'conflicting-options'
        elif nodeName_ == 'prerequisite-options':
            obj_ = prerequisite_optionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.prerequisite_options = obj_
            obj_.original_tagname_ = 'prerequisite-options'
# end class option


class service(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service_code=None, service_name=None, comment=None, options=None, restrictions=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.service_code = service_code
        self.service_code_nsprefix_ = None
        self.service_name = service_name
        self.service_name_nsprefix_ = None
        self.comment = comment
        self.comment_nsprefix_ = None
        self.options = options
        self.options_nsprefix_ = None
        self.restrictions = restrictions
        self.restrictions_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, service)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if service.subclass:
            return service.subclass(*args_, **kwargs_)
        else:
            return service(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_service_code(self):
        return self.service_code
    def set_service_code(self, service_code):
        self.service_code = service_code
    def get_service_name(self):
        return self.service_name
    def set_service_name(self, service_name):
        self.service_name = service_name
    def get_comment(self):
        return self.comment
    def set_comment(self, comment):
        self.comment = comment
    def get_options(self):
        return self.options
    def set_options(self, options):
        self.options = options
    def get_restrictions(self):
        return self.restrictions
    def set_restrictions(self, restrictions):
        self.restrictions = restrictions
    def _hasContent(self):
        if (
            self.service_code is not None or
            self.service_name is not None or
            self.comment is not None or
            self.options is not None or
            self.restrictions is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='service', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('service')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'service':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='service')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='service', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='service'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='service', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.service_code is not None:
            namespaceprefix_ = self.service_code_nsprefix_ + ':' if (UseCapturedNS_ and self.service_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-code>%s</%sservice-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_code), input_name='service-code')), namespaceprefix_ , eol_))
        if self.service_name is not None:
            namespaceprefix_ = self.service_name_nsprefix_ + ':' if (UseCapturedNS_ and self.service_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-name>%s</%sservice-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_name), input_name='service-name')), namespaceprefix_ , eol_))
        if self.comment is not None:
            namespaceprefix_ = self.comment_nsprefix_ + ':' if (UseCapturedNS_ and self.comment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scomment>%s</%scomment>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.comment), input_name='comment')), namespaceprefix_ , eol_))
        if self.options is not None:
            namespaceprefix_ = self.options_nsprefix_ + ':' if (UseCapturedNS_ and self.options_nsprefix_) else ''
            self.options.export(outfile, level, namespaceprefix_, namespacedef_='', name_='options', pretty_print=pretty_print)
        if self.restrictions is not None:
            namespaceprefix_ = self.restrictions_nsprefix_ + ':' if (UseCapturedNS_ and self.restrictions_nsprefix_) else ''
            self.restrictions.export(outfile, level, namespaceprefix_, namespacedef_='', name_='restrictions', pretty_print=pretty_print)
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
        elif nodeName_ == 'service-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'service_name')
            value_ = self.gds_validate_string(value_, node, 'service_name')
            self.service_name = value_
            self.service_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'comment':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'comment')
            value_ = self.gds_validate_string(value_, node, 'comment')
            self.comment = value_
            self.comment_nsprefix_ = child_.prefix
        elif nodeName_ == 'options':
            obj_ = optionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.options = obj_
            obj_.original_tagname_ = 'options'
        elif nodeName_ == 'restrictions':
            obj_ = restrictionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.restrictions = obj_
            obj_.original_tagname_ = 'restrictions'
# end class service


class options(GeneratedsSuper):
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
                CurrentSubclassModule_, options)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if options.subclass:
            return options.subclass(*args_, **kwargs_)
        else:
            return options(*args_, **kwargs_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='options', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('options')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'options':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='options')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='options', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='options'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='options', fromsubclass_=False, pretty_print=True):
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
            obj_ = optionType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.option.append(obj_)
            obj_.original_tagname_ = 'option'
# end class options


class NumberRangeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, min=None, max=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.min = _cast(float, min)
        self.min_nsprefix_ = None
        self.max = _cast(float, max)
        self.max_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NumberRangeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NumberRangeType.subclass:
            return NumberRangeType.subclass(*args_, **kwargs_)
        else:
            return NumberRangeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_min(self):
        return self.min
    def set_min(self, min):
        self.min = min
    def get_max(self):
        return self.max
    def set_max(self, max):
        self.max = max
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NumberRangeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NumberRangeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NumberRangeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NumberRangeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NumberRangeType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NumberRangeType'):
        if self.min is not None and 'min' not in already_processed:
            already_processed.add('min')
            outfile.write(' min="%s"' % self.gds_format_decimal(self.min, input_name='min'))
        if self.max is not None and 'max' not in already_processed:
            already_processed.add('max')
            outfile.write(' max="%s"' % self.gds_format_decimal(self.max, input_name='max'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NumberRangeType', fromsubclass_=False, pretty_print=True):
        pass
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
        value = find_attr_value_('min', node)
        if value is not None and 'min' not in already_processed:
            already_processed.add('min')
            value = self.gds_parse_decimal(value, node, 'min')
            self.min = value
        value = find_attr_value_('max', node)
        if value is not None and 'max' not in already_processed:
            already_processed.add('max')
            value = self.gds_parse_decimal(value, node, 'max')
            self.max = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class NumberRangeType


class serviceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service_code=None, service_name=None, link=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.service_code = service_code
        self.service_code_nsprefix_ = None
        self.service_name = service_name
        self.service_name_nsprefix_ = None
        self.link = link
        self.link_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, serviceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if serviceType.subclass:
            return serviceType.subclass(*args_, **kwargs_)
        else:
            return serviceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_service_code(self):
        return self.service_code
    def set_service_code(self, service_code):
        self.service_code = service_code
    def get_service_name(self):
        return self.service_name
    def set_service_name(self, service_name):
        self.service_name = service_name
    def get_link(self):
        return self.link
    def set_link(self, link):
        self.link = link
    def _hasContent(self):
        if (
            self.service_code is not None or
            self.service_name is not None or
            self.link is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='serviceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('serviceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'serviceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='serviceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='serviceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='serviceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='serviceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.service_code is not None:
            namespaceprefix_ = self.service_code_nsprefix_ + ':' if (UseCapturedNS_ and self.service_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-code>%s</%sservice-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_code), input_name='service-code')), namespaceprefix_ , eol_))
        if self.service_name is not None:
            namespaceprefix_ = self.service_name_nsprefix_ + ':' if (UseCapturedNS_ and self.service_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-name>%s</%sservice-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_name), input_name='service-name')), namespaceprefix_ , eol_))
        if self.link is not None:
            namespaceprefix_ = self.link_nsprefix_ + ':' if (UseCapturedNS_ and self.link_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slink>%s</%slink>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.link), input_name='link')), namespaceprefix_ , eol_))
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
        elif nodeName_ == 'service-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'service_name')
            value_ = self.gds_validate_string(value_, node, 'service_name')
            self.service_name = value_
            self.service_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'link':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'link')
            value_ = self.gds_validate_string(value_, node, 'link')
            self.link = value_
            self.link_nsprefix_ = child_.prefix
# end class serviceType


class conflicting_optionsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, option_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if option_code is None:
            self.option_code = []
        else:
            self.option_code = option_code
        self.option_code_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, conflicting_optionsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if conflicting_optionsType.subclass:
            return conflicting_optionsType.subclass(*args_, **kwargs_)
        else:
            return conflicting_optionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_option_code(self):
        return self.option_code
    def set_option_code(self, option_code):
        self.option_code = option_code
    def add_option_code(self, value):
        self.option_code.append(value)
    def insert_option_code_at(self, index, value):
        self.option_code.insert(index, value)
    def replace_option_code_at(self, index, value):
        self.option_code[index] = value
    def _hasContent(self):
        if (
            self.option_code
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='conflicting-optionsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('conflicting-optionsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'conflicting-optionsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='conflicting-optionsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='conflicting-optionsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='conflicting-optionsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='conflicting-optionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for option_code_ in self.option_code:
            namespaceprefix_ = self.option_code_nsprefix_ + ':' if (UseCapturedNS_ and self.option_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-code>%s</%soption-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(option_code_), input_name='option-code')), namespaceprefix_ , eol_))
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
            self.option_code.append(value_)
            self.option_code_nsprefix_ = child_.prefix
# end class conflicting_optionsType


class prerequisite_optionsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, option_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if option_code is None:
            self.option_code = []
        else:
            self.option_code = option_code
        self.option_code_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, prerequisite_optionsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if prerequisite_optionsType.subclass:
            return prerequisite_optionsType.subclass(*args_, **kwargs_)
        else:
            return prerequisite_optionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_option_code(self):
        return self.option_code
    def set_option_code(self, option_code):
        self.option_code = option_code
    def add_option_code(self, value):
        self.option_code.append(value)
    def insert_option_code_at(self, index, value):
        self.option_code.insert(index, value)
    def replace_option_code_at(self, index, value):
        self.option_code[index] = value
    def _hasContent(self):
        if (
            self.option_code
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='prerequisite-optionsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('prerequisite-optionsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'prerequisite-optionsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='prerequisite-optionsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='prerequisite-optionsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='prerequisite-optionsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='prerequisite-optionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for option_code_ in self.option_code:
            namespaceprefix_ = self.option_code_nsprefix_ + ':' if (UseCapturedNS_ and self.option_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-code>%s</%soption-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(option_code_), input_name='option-code')), namespaceprefix_ , eol_))
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
            self.option_code.append(value_)
            self.option_code_nsprefix_ = child_.prefix
# end class prerequisite_optionsType


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
    def __init__(self, option_code=None, option_name=None, link=None, mandatory=None, qualifier_required=None, qualifier_max=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.option_code = option_code
        self.option_code_nsprefix_ = None
        self.option_name = option_name
        self.option_name_nsprefix_ = None
        self.link = link
        self.link_nsprefix_ = None
        self.mandatory = mandatory
        self.mandatory_nsprefix_ = None
        self.qualifier_required = qualifier_required
        self.qualifier_required_nsprefix_ = None
        self.qualifier_max = qualifier_max
        self.qualifier_max_nsprefix_ = None
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
    def get_option_name(self):
        return self.option_name
    def set_option_name(self, option_name):
        self.option_name = option_name
    def get_link(self):
        return self.link
    def set_link(self, link):
        self.link = link
    def get_mandatory(self):
        return self.mandatory
    def set_mandatory(self, mandatory):
        self.mandatory = mandatory
    def get_qualifier_required(self):
        return self.qualifier_required
    def set_qualifier_required(self, qualifier_required):
        self.qualifier_required = qualifier_required
    def get_qualifier_max(self):
        return self.qualifier_max
    def set_qualifier_max(self, qualifier_max):
        self.qualifier_max = qualifier_max
    def _hasContent(self):
        if (
            self.option_code is not None or
            self.option_name is not None or
            self.link is not None or
            self.mandatory is not None or
            self.qualifier_required is not None or
            self.qualifier_max is not None
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
        if self.option_name is not None:
            namespaceprefix_ = self.option_name_nsprefix_ + ':' if (UseCapturedNS_ and self.option_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-name>%s</%soption-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.option_name), input_name='option-name')), namespaceprefix_ , eol_))
        if self.link is not None:
            namespaceprefix_ = self.link_nsprefix_ + ':' if (UseCapturedNS_ and self.link_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slink>%s</%slink>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.link), input_name='link')), namespaceprefix_ , eol_))
        if self.mandatory is not None:
            namespaceprefix_ = self.mandatory_nsprefix_ + ':' if (UseCapturedNS_ and self.mandatory_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smandatory>%s</%smandatory>%s' % (namespaceprefix_ , self.gds_format_boolean(self.mandatory, input_name='mandatory'), namespaceprefix_ , eol_))
        if self.qualifier_required is not None:
            namespaceprefix_ = self.qualifier_required_nsprefix_ + ':' if (UseCapturedNS_ and self.qualifier_required_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%squalifier-required>%s</%squalifier-required>%s' % (namespaceprefix_ , self.gds_format_boolean(self.qualifier_required, input_name='qualifier-required'), namespaceprefix_ , eol_))
        if self.qualifier_max is not None:
            namespaceprefix_ = self.qualifier_max_nsprefix_ + ':' if (UseCapturedNS_ and self.qualifier_max_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%squalifier-max>%s</%squalifier-max>%s' % (namespaceprefix_ , self.gds_format_decimal(self.qualifier_max, input_name='qualifier-max'), namespaceprefix_ , eol_))
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
        elif nodeName_ == 'link':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'link')
            value_ = self.gds_validate_string(value_, node, 'link')
            self.link = value_
            self.link_nsprefix_ = child_.prefix
        elif nodeName_ == 'mandatory':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'mandatory')
            ival_ = self.gds_validate_boolean(ival_, node, 'mandatory')
            self.mandatory = ival_
            self.mandatory_nsprefix_ = child_.prefix
        elif nodeName_ == 'qualifier-required':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'qualifier_required')
            ival_ = self.gds_validate_boolean(ival_, node, 'qualifier_required')
            self.qualifier_required = ival_
            self.qualifier_required_nsprefix_ = child_.prefix
        elif nodeName_ == 'qualifier-max' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'qualifier_max')
            fval_ = self.gds_validate_decimal(fval_, node, 'qualifier_max')
            self.qualifier_max = fval_
            self.qualifier_max_nsprefix_ = child_.prefix
# end class optionType


class restrictionsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, weight_restriction=None, dimensional_restrictions=None, density_factor=None, can_ship_in_mailing_tube=None, can_ship_unpackaged=None, allowed_as_return_service=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.weight_restriction = weight_restriction
        self.weight_restriction_nsprefix_ = None
        self.dimensional_restrictions = dimensional_restrictions
        self.dimensional_restrictions_nsprefix_ = None
        self.density_factor = density_factor
        self.density_factor_nsprefix_ = None
        self.can_ship_in_mailing_tube = can_ship_in_mailing_tube
        self.can_ship_in_mailing_tube_nsprefix_ = None
        self.can_ship_unpackaged = can_ship_unpackaged
        self.can_ship_unpackaged_nsprefix_ = None
        self.allowed_as_return_service = allowed_as_return_service
        self.allowed_as_return_service_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, restrictionsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if restrictionsType.subclass:
            return restrictionsType.subclass(*args_, **kwargs_)
        else:
            return restrictionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_weight_restriction(self):
        return self.weight_restriction
    def set_weight_restriction(self, weight_restriction):
        self.weight_restriction = weight_restriction
    def get_dimensional_restrictions(self):
        return self.dimensional_restrictions
    def set_dimensional_restrictions(self, dimensional_restrictions):
        self.dimensional_restrictions = dimensional_restrictions
    def get_density_factor(self):
        return self.density_factor
    def set_density_factor(self, density_factor):
        self.density_factor = density_factor
    def get_can_ship_in_mailing_tube(self):
        return self.can_ship_in_mailing_tube
    def set_can_ship_in_mailing_tube(self, can_ship_in_mailing_tube):
        self.can_ship_in_mailing_tube = can_ship_in_mailing_tube
    def get_can_ship_unpackaged(self):
        return self.can_ship_unpackaged
    def set_can_ship_unpackaged(self, can_ship_unpackaged):
        self.can_ship_unpackaged = can_ship_unpackaged
    def get_allowed_as_return_service(self):
        return self.allowed_as_return_service
    def set_allowed_as_return_service(self, allowed_as_return_service):
        self.allowed_as_return_service = allowed_as_return_service
    def _hasContent(self):
        if (
            self.weight_restriction is not None or
            self.dimensional_restrictions is not None or
            self.density_factor is not None or
            self.can_ship_in_mailing_tube is not None or
            self.can_ship_unpackaged is not None or
            self.allowed_as_return_service is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='restrictionsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('restrictionsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'restrictionsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='restrictionsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='restrictionsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='restrictionsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='restrictionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.weight_restriction is not None:
            namespaceprefix_ = self.weight_restriction_nsprefix_ + ':' if (UseCapturedNS_ and self.weight_restriction_nsprefix_) else ''
            self.weight_restriction.export(outfile, level, namespaceprefix_, namespacedef_='', name_='weight-restriction', pretty_print=pretty_print)
        if self.dimensional_restrictions is not None:
            namespaceprefix_ = self.dimensional_restrictions_nsprefix_ + ':' if (UseCapturedNS_ and self.dimensional_restrictions_nsprefix_) else ''
            self.dimensional_restrictions.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dimensional-restrictions', pretty_print=pretty_print)
        if self.density_factor is not None:
            namespaceprefix_ = self.density_factor_nsprefix_ + ':' if (UseCapturedNS_ and self.density_factor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdensity-factor>%s</%sdensity-factor>%s' % (namespaceprefix_ , self.gds_format_decimal(self.density_factor, input_name='density-factor'), namespaceprefix_ , eol_))
        if self.can_ship_in_mailing_tube is not None:
            namespaceprefix_ = self.can_ship_in_mailing_tube_nsprefix_ + ':' if (UseCapturedNS_ and self.can_ship_in_mailing_tube_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scan-ship-in-mailing-tube>%s</%scan-ship-in-mailing-tube>%s' % (namespaceprefix_ , self.gds_format_boolean(self.can_ship_in_mailing_tube, input_name='can-ship-in-mailing-tube'), namespaceprefix_ , eol_))
        if self.can_ship_unpackaged is not None:
            namespaceprefix_ = self.can_ship_unpackaged_nsprefix_ + ':' if (UseCapturedNS_ and self.can_ship_unpackaged_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scan-ship-unpackaged>%s</%scan-ship-unpackaged>%s' % (namespaceprefix_ , self.gds_format_boolean(self.can_ship_unpackaged, input_name='can-ship-unpackaged'), namespaceprefix_ , eol_))
        if self.allowed_as_return_service is not None:
            namespaceprefix_ = self.allowed_as_return_service_nsprefix_ + ':' if (UseCapturedNS_ and self.allowed_as_return_service_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sallowed-as-return-service>%s</%sallowed-as-return-service>%s' % (namespaceprefix_ , self.gds_format_boolean(self.allowed_as_return_service, input_name='allowed-as-return-service'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'weight-restriction':
            obj_ = NumberRangeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.weight_restriction = obj_
            obj_.original_tagname_ = 'weight-restriction'
        elif nodeName_ == 'dimensional-restrictions':
            obj_ = dimensional_restrictionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dimensional_restrictions = obj_
            obj_.original_tagname_ = 'dimensional-restrictions'
        elif nodeName_ == 'density-factor' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'density_factor')
            fval_ = self.gds_validate_decimal(fval_, node, 'density_factor')
            self.density_factor = fval_
            self.density_factor_nsprefix_ = child_.prefix
        elif nodeName_ == 'can-ship-in-mailing-tube':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'can_ship_in_mailing_tube')
            ival_ = self.gds_validate_boolean(ival_, node, 'can_ship_in_mailing_tube')
            self.can_ship_in_mailing_tube = ival_
            self.can_ship_in_mailing_tube_nsprefix_ = child_.prefix
        elif nodeName_ == 'can-ship-unpackaged':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'can_ship_unpackaged')
            ival_ = self.gds_validate_boolean(ival_, node, 'can_ship_unpackaged')
            self.can_ship_unpackaged = ival_
            self.can_ship_unpackaged_nsprefix_ = child_.prefix
        elif nodeName_ == 'allowed-as-return-service':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'allowed_as_return_service')
            ival_ = self.gds_validate_boolean(ival_, node, 'allowed_as_return_service')
            self.allowed_as_return_service = ival_
            self.allowed_as_return_service_nsprefix_ = child_.prefix
# end class restrictionsType


class dimensional_restrictionsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, length=None, width=None, height=None, length_plus_girth_max=None, length_height_width_sum_max=None, oversize_limit=None, gds_collector_=None, **kwargs_):
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
        self.length_plus_girth_max = length_plus_girth_max
        self.length_plus_girth_max_nsprefix_ = None
        self.length_height_width_sum_max = length_height_width_sum_max
        self.length_height_width_sum_max_nsprefix_ = None
        self.oversize_limit = oversize_limit
        self.oversize_limit_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dimensional_restrictionsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dimensional_restrictionsType.subclass:
            return dimensional_restrictionsType.subclass(*args_, **kwargs_)
        else:
            return dimensional_restrictionsType(*args_, **kwargs_)
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
    def get_length_plus_girth_max(self):
        return self.length_plus_girth_max
    def set_length_plus_girth_max(self, length_plus_girth_max):
        self.length_plus_girth_max = length_plus_girth_max
    def get_length_height_width_sum_max(self):
        return self.length_height_width_sum_max
    def set_length_height_width_sum_max(self, length_height_width_sum_max):
        self.length_height_width_sum_max = length_height_width_sum_max
    def get_oversize_limit(self):
        return self.oversize_limit
    def set_oversize_limit(self, oversize_limit):
        self.oversize_limit = oversize_limit
    def _hasContent(self):
        if (
            self.length is not None or
            self.width is not None or
            self.height is not None or
            self.length_plus_girth_max is not None or
            self.length_height_width_sum_max is not None or
            self.oversize_limit is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='dimensional-restrictionsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dimensional-restrictionsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dimensional-restrictionsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dimensional-restrictionsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dimensional-restrictionsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dimensional-restrictionsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='dimensional-restrictionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.length is not None:
            namespaceprefix_ = self.length_nsprefix_ + ':' if (UseCapturedNS_ and self.length_nsprefix_) else ''
            self.length.export(outfile, level, namespaceprefix_, namespacedef_='', name_='length', pretty_print=pretty_print)
        if self.width is not None:
            namespaceprefix_ = self.width_nsprefix_ + ':' if (UseCapturedNS_ and self.width_nsprefix_) else ''
            self.width.export(outfile, level, namespaceprefix_, namespacedef_='', name_='width', pretty_print=pretty_print)
        if self.height is not None:
            namespaceprefix_ = self.height_nsprefix_ + ':' if (UseCapturedNS_ and self.height_nsprefix_) else ''
            self.height.export(outfile, level, namespaceprefix_, namespacedef_='', name_='height', pretty_print=pretty_print)
        if self.length_plus_girth_max is not None:
            namespaceprefix_ = self.length_plus_girth_max_nsprefix_ + ':' if (UseCapturedNS_ and self.length_plus_girth_max_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slength-plus-girth-max>%s</%slength-plus-girth-max>%s' % (namespaceprefix_ , self.gds_format_decimal(self.length_plus_girth_max, input_name='length-plus-girth-max'), namespaceprefix_ , eol_))
        if self.length_height_width_sum_max is not None:
            namespaceprefix_ = self.length_height_width_sum_max_nsprefix_ + ':' if (UseCapturedNS_ and self.length_height_width_sum_max_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slength-height-width-sum-max>%s</%slength-height-width-sum-max>%s' % (namespaceprefix_ , self.gds_format_decimal(self.length_height_width_sum_max, input_name='length-height-width-sum-max'), namespaceprefix_ , eol_))
        if self.oversize_limit is not None:
            namespaceprefix_ = self.oversize_limit_nsprefix_ + ':' if (UseCapturedNS_ and self.oversize_limit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soversize-limit>%s</%soversize-limit>%s' % (namespaceprefix_ , self.gds_format_decimal(self.oversize_limit, input_name='oversize-limit'), namespaceprefix_ , eol_))
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
            obj_ = NumberRangeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.length = obj_
            obj_.original_tagname_ = 'length'
        elif nodeName_ == 'width':
            obj_ = NumberRangeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.width = obj_
            obj_.original_tagname_ = 'width'
        elif nodeName_ == 'height':
            obj_ = NumberRangeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.height = obj_
            obj_.original_tagname_ = 'height'
        elif nodeName_ == 'length-plus-girth-max' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'length_plus_girth_max')
            fval_ = self.gds_validate_decimal(fval_, node, 'length_plus_girth_max')
            self.length_plus_girth_max = fval_
            self.length_plus_girth_max_nsprefix_ = child_.prefix
        elif nodeName_ == 'length-height-width-sum-max' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'length_height_width_sum_max')
            fval_ = self.gds_validate_decimal(fval_, node, 'length_height_width_sum_max')
            self.length_height_width_sum_max = fval_
            self.length_height_width_sum_max_nsprefix_ = child_.prefix
        elif nodeName_ == 'oversize-limit' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'oversize_limit')
            fval_ = self.gds_validate_decimal(fval_, node, 'oversize_limit')
            self.oversize_limit = fval_
            self.oversize_limit_nsprefix_ = child_.prefix
# end class dimensional_restrictionsType


class optionType1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, option_code=None, option_name=None, link=None, qualifier_required=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.option_code = option_code
        self.option_code_nsprefix_ = None
        self.option_name = option_name
        self.option_name_nsprefix_ = None
        self.link = link
        self.link_nsprefix_ = None
        self.qualifier_required = qualifier_required
        self.qualifier_required_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, optionType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if optionType1.subclass:
            return optionType1.subclass(*args_, **kwargs_)
        else:
            return optionType1(*args_, **kwargs_)
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
    def get_link(self):
        return self.link
    def set_link(self, link):
        self.link = link
    def get_qualifier_required(self):
        return self.qualifier_required
    def set_qualifier_required(self, qualifier_required):
        self.qualifier_required = qualifier_required
    def _hasContent(self):
        if (
            self.option_code is not None or
            self.option_name is not None or
            self.link is not None or
            self.qualifier_required is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='optionType1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('optionType1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'optionType1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='optionType1')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='optionType1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='optionType1'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='optionType1', fromsubclass_=False, pretty_print=True):
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
        if self.link is not None:
            namespaceprefix_ = self.link_nsprefix_ + ':' if (UseCapturedNS_ and self.link_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slink>%s</%slink>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.link), input_name='link')), namespaceprefix_ , eol_))
        if self.qualifier_required is not None:
            namespaceprefix_ = self.qualifier_required_nsprefix_ + ':' if (UseCapturedNS_ and self.qualifier_required_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%squalifier-required>%s</%squalifier-required>%s' % (namespaceprefix_ , self.gds_format_boolean(self.qualifier_required, input_name='qualifier-required'), namespaceprefix_ , eol_))
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
            if value_:
                value_ = re_.sub(String_cleanup_pat_, " ", value_).strip()
            else:
                value_ = ""
            value_ = self.gds_parse_string(value_, node, 'option_code')
            value_ = self.gds_validate_string(value_, node, 'option_code')
            self.option_code = value_
            self.option_code_nsprefix_ = child_.prefix
        elif nodeName_ == 'option-name':
            value_ = child_.text
            if value_:
                value_ = re_.sub(String_cleanup_pat_, " ", value_).strip()
            else:
                value_ = ""
            value_ = self.gds_parse_string(value_, node, 'option_name')
            value_ = self.gds_validate_string(value_, node, 'option_name')
            self.option_name = value_
            self.option_name_nsprefix_ = child_.prefix
        elif nodeName_ == 'link':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'link')
            value_ = self.gds_validate_string(value_, node, 'link')
            self.link = value_
            self.link_nsprefix_ = child_.prefix
        elif nodeName_ == 'qualifier-required':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'qualifier_required')
            ival_ = self.gds_validate_boolean(ival_, node, 'qualifier_required')
            self.qualifier_required = ival_
            self.qualifier_required_nsprefix_ = child_.prefix
# end class optionType1


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
        rootTag = 'services'
        rootClass = services
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
        rootTag = 'services'
        rootClass = services
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
        rootTag = 'services'
        rootClass = services
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
        rootTag = 'services'
        rootClass = services
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from discovery import *\n\n')
        sys.stdout.write('import discovery as model_\n\n')
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
NamespaceToDefMappings_ = {'http://www.canadapost.ca/ws/ship/rate-v4': [('NumberRangeType',
                                               './schemas/discovery.xsd',
                                               'CT')]}

__all__ = [
    "NumberRangeType",
    "conflicting_optionsType",
    "dimensional_restrictionsType",
    "option",
    "optionType",
    "optionType1",
    "options",
    "optionsType",
    "prerequisite_optionsType",
    "restrictionsType",
    "service",
    "serviceType",
    "services"
]
