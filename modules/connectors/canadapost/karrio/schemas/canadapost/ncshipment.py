#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Jul 14 15:39:44 2021 by generateDS.py version 2.39.2.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './canadapost_lib/ncshipment.py')
#
# Command line arguments:
#   ./schemas/ncshipment.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-carriers/.venv/karrio-carriers/bin/generateDS --no-namespace-defs -o "./canadapost_lib/ncshipment.py" ./schemas/ncshipment.xsd
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
    SELF='self'
    DETAILS='details'
    SHIPMENT='shipment'
    RECEIPT='receipt'
    REFUND='refund'
    LABEL='label'
    COD_REMITTANCE_LABEL='codRemittanceLabel'
    COD_RECORD_OF_DELIVERY='codRecordOfDelivery'
    COMMERCIAL_INVOICE='commercialInvoice'


class NonContractShipmentInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, shipment_id=None, tracking_pin=None, links=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.shipment_id = shipment_id
        self.validate_ShipmentIDType(self.shipment_id)
        self.shipment_id_nsprefix_ = None
        self.tracking_pin = tracking_pin
        self.validate_TrackingPINType(self.tracking_pin)
        self.tracking_pin_nsprefix_ = None
        self.links = links
        self.links_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonContractShipmentInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonContractShipmentInfoType.subclass:
            return NonContractShipmentInfoType.subclass(*args_, **kwargs_)
        else:
            return NonContractShipmentInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_shipment_id(self):
        return self.shipment_id
    def set_shipment_id(self, shipment_id):
        self.shipment_id = shipment_id
    def get_tracking_pin(self):
        return self.tracking_pin
    def set_tracking_pin(self, tracking_pin):
        self.tracking_pin = tracking_pin
    def get_links(self):
        return self.links
    def set_links(self, links):
        self.links = links
    def validate_ShipmentIDType(self, value):
        result = True
        # Validate type ShipmentIDType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ShipmentIDType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_TrackingPINType(self, value):
        result = True
        # Validate type TrackingPINType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TrackingPINType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 11:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TrackingPINType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.shipment_id is not None or
            self.tracking_pin is not None or
            self.links is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonContractShipmentInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonContractShipmentInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonContractShipmentInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonContractShipmentInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonContractShipmentInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.shipment_id is not None:
            namespaceprefix_ = self.shipment_id_nsprefix_ + ':' if (UseCapturedNS_ and self.shipment_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshipment-id>%s</%sshipment-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.shipment_id), input_name='shipment-id')), namespaceprefix_ , eol_))
        if self.tracking_pin is not None:
            namespaceprefix_ = self.tracking_pin_nsprefix_ + ':' if (UseCapturedNS_ and self.tracking_pin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stracking-pin>%s</%stracking-pin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tracking_pin), input_name='tracking-pin')), namespaceprefix_ , eol_))
        if self.links is not None:
            namespaceprefix_ = self.links_nsprefix_ + ':' if (UseCapturedNS_ and self.links_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slinks>%s</%slinks>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.links), input_name='links')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'shipment-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shipment_id')
            value_ = self.gds_validate_string(value_, node, 'shipment_id')
            self.shipment_id = value_
            self.shipment_id_nsprefix_ = child_.prefix
            # validate type ShipmentIDType
            self.validate_ShipmentIDType(self.shipment_id)
        elif nodeName_ == 'tracking-pin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tracking_pin')
            value_ = self.gds_validate_string(value_, node, 'tracking_pin')
            self.tracking_pin = value_
            self.tracking_pin_nsprefix_ = child_.prefix
            # validate type TrackingPINType
            self.validate_TrackingPINType(self.tracking_pin)
        elif nodeName_ == 'links':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'links')
            value_ = self.gds_validate_string(value_, node, 'links')
            self.links = value_
            self.links_nsprefix_ = child_.prefix
# end class NonContractShipmentInfoType


class NonContractShipmentDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, final_shipping_point=None, tracking_pin=None, delivery_spec=None, refund_request_info=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.final_shipping_point = final_shipping_point
        self.final_shipping_point_nsprefix_ = None
        self.tracking_pin = tracking_pin
        self.validate_TrackingPINType(self.tracking_pin)
        self.tracking_pin_nsprefix_ = None
        self.delivery_spec = delivery_spec
        self.delivery_spec_nsprefix_ = None
        self.refund_request_info = refund_request_info
        self.refund_request_info_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonContractShipmentDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonContractShipmentDetailsType.subclass:
            return NonContractShipmentDetailsType.subclass(*args_, **kwargs_)
        else:
            return NonContractShipmentDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_final_shipping_point(self):
        return self.final_shipping_point
    def set_final_shipping_point(self, final_shipping_point):
        self.final_shipping_point = final_shipping_point
    def get_tracking_pin(self):
        return self.tracking_pin
    def set_tracking_pin(self, tracking_pin):
        self.tracking_pin = tracking_pin
    def get_delivery_spec(self):
        return self.delivery_spec
    def set_delivery_spec(self, delivery_spec):
        self.delivery_spec = delivery_spec
    def get_refund_request_info(self):
        return self.refund_request_info
    def set_refund_request_info(self, refund_request_info):
        self.refund_request_info = refund_request_info
    def validate_TrackingPINType(self, value):
        result = True
        # Validate type TrackingPINType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TrackingPINType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 11:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TrackingPINType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.final_shipping_point is not None or
            self.tracking_pin is not None or
            self.delivery_spec is not None or
            self.refund_request_info is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonContractShipmentDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonContractShipmentDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonContractShipmentDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonContractShipmentDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonContractShipmentDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.final_shipping_point is not None:
            namespaceprefix_ = self.final_shipping_point_nsprefix_ + ':' if (UseCapturedNS_ and self.final_shipping_point_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfinal-shipping-point>%s</%sfinal-shipping-point>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.final_shipping_point), input_name='final-shipping-point')), namespaceprefix_ , eol_))
        if self.tracking_pin is not None:
            namespaceprefix_ = self.tracking_pin_nsprefix_ + ':' if (UseCapturedNS_ and self.tracking_pin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stracking-pin>%s</%stracking-pin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tracking_pin), input_name='tracking-pin')), namespaceprefix_ , eol_))
        if self.delivery_spec is not None:
            namespaceprefix_ = self.delivery_spec_nsprefix_ + ':' if (UseCapturedNS_ and self.delivery_spec_nsprefix_) else ''
            self.delivery_spec.export(outfile, level, namespaceprefix_, namespacedef_='', name_='delivery-spec', pretty_print=pretty_print)
        if self.refund_request_info is not None:
            namespaceprefix_ = self.refund_request_info_nsprefix_ + ':' if (UseCapturedNS_ and self.refund_request_info_nsprefix_) else ''
            self.refund_request_info.export(outfile, level, namespaceprefix_, namespacedef_='', name_='refund-request-info', pretty_print=pretty_print)
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
        if nodeName_ == 'final-shipping-point':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'final_shipping_point')
            value_ = self.gds_validate_string(value_, node, 'final_shipping_point')
            self.final_shipping_point = value_
            self.final_shipping_point_nsprefix_ = child_.prefix
        elif nodeName_ == 'tracking-pin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tracking_pin')
            value_ = self.gds_validate_string(value_, node, 'tracking_pin')
            self.tracking_pin = value_
            self.tracking_pin_nsprefix_ = child_.prefix
            # validate type TrackingPINType
            self.validate_TrackingPINType(self.tracking_pin)
        elif nodeName_ == 'delivery-spec':
            obj_ = delivery_specType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.delivery_spec = obj_
            obj_.original_tagname_ = 'delivery-spec'
        elif nodeName_ == 'refund-request-info':
            obj_ = NonContractShipmentRefundRequestInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.refund_request_info = obj_
            obj_.original_tagname_ = 'refund-request-info'
# end class NonContractShipmentDetailsType


class NonContractShipmentReceiptType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, final_shipping_point=None, shipping_point_name=None, shipping_point_id=None, mailed_by_customer=None, service_code=None, rated_weight=None, base_amount=None, pre_tax_amount=None, gst_amount=None, pst_amount=None, hst_amount=None, priced_options=None, adjustments=None, cc_receipt_details=None, service_standard=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.final_shipping_point = final_shipping_point
        self.final_shipping_point_nsprefix_ = None
        self.shipping_point_name = shipping_point_name
        self.validate_shipping_point_nameType(self.shipping_point_name)
        self.shipping_point_name_nsprefix_ = None
        self.shipping_point_id = shipping_point_id
        self.shipping_point_id_nsprefix_ = None
        self.mailed_by_customer = mailed_by_customer
        self.mailed_by_customer_nsprefix_ = None
        self.service_code = service_code
        self.service_code_nsprefix_ = None
        self.rated_weight = rated_weight
        self.validate_rated_weightType(self.rated_weight)
        self.rated_weight_nsprefix_ = None
        self.base_amount = base_amount
        self.base_amount_nsprefix_ = None
        self.pre_tax_amount = pre_tax_amount
        self.pre_tax_amount_nsprefix_ = None
        self.gst_amount = gst_amount
        self.gst_amount_nsprefix_ = None
        self.pst_amount = pst_amount
        self.pst_amount_nsprefix_ = None
        self.hst_amount = hst_amount
        self.hst_amount_nsprefix_ = None
        self.priced_options = priced_options
        self.priced_options_nsprefix_ = None
        self.adjustments = adjustments
        self.adjustments_nsprefix_ = None
        self.cc_receipt_details = cc_receipt_details
        self.cc_receipt_details_nsprefix_ = None
        self.service_standard = service_standard
        self.service_standard_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonContractShipmentReceiptType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonContractShipmentReceiptType.subclass:
            return NonContractShipmentReceiptType.subclass(*args_, **kwargs_)
        else:
            return NonContractShipmentReceiptType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_final_shipping_point(self):
        return self.final_shipping_point
    def set_final_shipping_point(self, final_shipping_point):
        self.final_shipping_point = final_shipping_point
    def get_shipping_point_name(self):
        return self.shipping_point_name
    def set_shipping_point_name(self, shipping_point_name):
        self.shipping_point_name = shipping_point_name
    def get_shipping_point_id(self):
        return self.shipping_point_id
    def set_shipping_point_id(self, shipping_point_id):
        self.shipping_point_id = shipping_point_id
    def get_mailed_by_customer(self):
        return self.mailed_by_customer
    def set_mailed_by_customer(self, mailed_by_customer):
        self.mailed_by_customer = mailed_by_customer
    def get_service_code(self):
        return self.service_code
    def set_service_code(self, service_code):
        self.service_code = service_code
    def get_rated_weight(self):
        return self.rated_weight
    def set_rated_weight(self, rated_weight):
        self.rated_weight = rated_weight
    def get_base_amount(self):
        return self.base_amount
    def set_base_amount(self, base_amount):
        self.base_amount = base_amount
    def get_pre_tax_amount(self):
        return self.pre_tax_amount
    def set_pre_tax_amount(self, pre_tax_amount):
        self.pre_tax_amount = pre_tax_amount
    def get_gst_amount(self):
        return self.gst_amount
    def set_gst_amount(self, gst_amount):
        self.gst_amount = gst_amount
    def get_pst_amount(self):
        return self.pst_amount
    def set_pst_amount(self, pst_amount):
        self.pst_amount = pst_amount
    def get_hst_amount(self):
        return self.hst_amount
    def set_hst_amount(self, hst_amount):
        self.hst_amount = hst_amount
    def get_priced_options(self):
        return self.priced_options
    def set_priced_options(self, priced_options):
        self.priced_options = priced_options
    def get_adjustments(self):
        return self.adjustments
    def set_adjustments(self, adjustments):
        self.adjustments = adjustments
    def get_cc_receipt_details(self):
        return self.cc_receipt_details
    def set_cc_receipt_details(self, cc_receipt_details):
        self.cc_receipt_details = cc_receipt_details
    def get_service_standard(self):
        return self.service_standard
    def set_service_standard(self, service_standard):
        self.service_standard = service_standard
    def validate_shipping_point_nameType(self, value):
        result = True
        # Validate type shipping-point-nameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 35:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on shipping-point-nameType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_rated_weightType(self, value):
        result = True
        # Validate type rated-weightType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value > 999.999:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on rated-weightType' % {"value": value, "lineno": lineno} )
                result = False
            if value <= 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minExclusive restriction on rated-weightType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.final_shipping_point is not None or
            self.shipping_point_name is not None or
            self.shipping_point_id is not None or
            self.mailed_by_customer is not None or
            self.service_code is not None or
            self.rated_weight is not None or
            self.base_amount is not None or
            self.pre_tax_amount is not None or
            self.gst_amount is not None or
            self.pst_amount is not None or
            self.hst_amount is not None or
            self.priced_options is not None or
            self.adjustments is not None or
            self.cc_receipt_details is not None or
            self.service_standard is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentReceiptType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonContractShipmentReceiptType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonContractShipmentReceiptType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonContractShipmentReceiptType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonContractShipmentReceiptType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonContractShipmentReceiptType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentReceiptType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.final_shipping_point is not None:
            namespaceprefix_ = self.final_shipping_point_nsprefix_ + ':' if (UseCapturedNS_ and self.final_shipping_point_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfinal-shipping-point>%s</%sfinal-shipping-point>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.final_shipping_point), input_name='final-shipping-point')), namespaceprefix_ , eol_))
        if self.shipping_point_name is not None:
            namespaceprefix_ = self.shipping_point_name_nsprefix_ + ':' if (UseCapturedNS_ and self.shipping_point_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshipping-point-name>%s</%sshipping-point-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.shipping_point_name), input_name='shipping-point-name')), namespaceprefix_ , eol_))
        if self.shipping_point_id is not None:
            namespaceprefix_ = self.shipping_point_id_nsprefix_ + ':' if (UseCapturedNS_ and self.shipping_point_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshipping-point-id>%s</%sshipping-point-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.shipping_point_id), input_name='shipping-point-id')), namespaceprefix_ , eol_))
        if self.mailed_by_customer is not None:
            namespaceprefix_ = self.mailed_by_customer_nsprefix_ + ':' if (UseCapturedNS_ and self.mailed_by_customer_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smailed-by-customer>%s</%smailed-by-customer>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.mailed_by_customer), input_name='mailed-by-customer')), namespaceprefix_ , eol_))
        if self.service_code is not None:
            namespaceprefix_ = self.service_code_nsprefix_ + ':' if (UseCapturedNS_ and self.service_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-code>%s</%sservice-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_code), input_name='service-code')), namespaceprefix_ , eol_))
        if self.rated_weight is not None:
            namespaceprefix_ = self.rated_weight_nsprefix_ + ':' if (UseCapturedNS_ and self.rated_weight_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srated-weight>%s</%srated-weight>%s' % (namespaceprefix_ , self.gds_format_decimal(self.rated_weight, input_name='rated-weight'), namespaceprefix_ , eol_))
        if self.base_amount is not None:
            namespaceprefix_ = self.base_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.base_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbase-amount>%s</%sbase-amount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.base_amount), input_name='base-amount')), namespaceprefix_ , eol_))
        if self.pre_tax_amount is not None:
            namespaceprefix_ = self.pre_tax_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.pre_tax_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spre-tax-amount>%s</%spre-tax-amount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pre_tax_amount), input_name='pre-tax-amount')), namespaceprefix_ , eol_))
        if self.gst_amount is not None:
            namespaceprefix_ = self.gst_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.gst_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgst-amount>%s</%sgst-amount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.gst_amount), input_name='gst-amount')), namespaceprefix_ , eol_))
        if self.pst_amount is not None:
            namespaceprefix_ = self.pst_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.pst_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spst-amount>%s</%spst-amount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pst_amount), input_name='pst-amount')), namespaceprefix_ , eol_))
        if self.hst_amount is not None:
            namespaceprefix_ = self.hst_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.hst_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shst-amount>%s</%shst-amount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.hst_amount), input_name='hst-amount')), namespaceprefix_ , eol_))
        if self.priced_options is not None:
            namespaceprefix_ = self.priced_options_nsprefix_ + ':' if (UseCapturedNS_ and self.priced_options_nsprefix_) else ''
            self.priced_options.export(outfile, level, namespaceprefix_, namespacedef_='', name_='priced-options', pretty_print=pretty_print)
        if self.adjustments is not None:
            namespaceprefix_ = self.adjustments_nsprefix_ + ':' if (UseCapturedNS_ and self.adjustments_nsprefix_) else ''
            self.adjustments.export(outfile, level, namespaceprefix_, namespacedef_='', name_='adjustments', pretty_print=pretty_print)
        if self.cc_receipt_details is not None:
            namespaceprefix_ = self.cc_receipt_details_nsprefix_ + ':' if (UseCapturedNS_ and self.cc_receipt_details_nsprefix_) else ''
            self.cc_receipt_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='cc-receipt-details', pretty_print=pretty_print)
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
        if nodeName_ == 'final-shipping-point':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'final_shipping_point')
            value_ = self.gds_validate_string(value_, node, 'final_shipping_point')
            self.final_shipping_point = value_
            self.final_shipping_point_nsprefix_ = child_.prefix
        elif nodeName_ == 'shipping-point-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shipping_point_name')
            value_ = self.gds_validate_string(value_, node, 'shipping_point_name')
            self.shipping_point_name = value_
            self.shipping_point_name_nsprefix_ = child_.prefix
            # validate type shipping-point-nameType
            self.validate_shipping_point_nameType(self.shipping_point_name)
        elif nodeName_ == 'shipping-point-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shipping_point_id')
            value_ = self.gds_validate_string(value_, node, 'shipping_point_id')
            self.shipping_point_id = value_
            self.shipping_point_id_nsprefix_ = child_.prefix
        elif nodeName_ == 'mailed-by-customer':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mailed_by_customer')
            value_ = self.gds_validate_string(value_, node, 'mailed_by_customer')
            self.mailed_by_customer = value_
            self.mailed_by_customer_nsprefix_ = child_.prefix
        elif nodeName_ == 'service-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'service_code')
            value_ = self.gds_validate_string(value_, node, 'service_code')
            self.service_code = value_
            self.service_code_nsprefix_ = child_.prefix
        elif nodeName_ == 'rated-weight' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'rated_weight')
            fval_ = self.gds_validate_decimal(fval_, node, 'rated_weight')
            self.rated_weight = fval_
            self.rated_weight_nsprefix_ = child_.prefix
            # validate type rated-weightType
            self.validate_rated_weightType(self.rated_weight)
        elif nodeName_ == 'base-amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'base_amount')
            value_ = self.gds_validate_string(value_, node, 'base_amount')
            self.base_amount = value_
            self.base_amount_nsprefix_ = child_.prefix
        elif nodeName_ == 'pre-tax-amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pre_tax_amount')
            value_ = self.gds_validate_string(value_, node, 'pre_tax_amount')
            self.pre_tax_amount = value_
            self.pre_tax_amount_nsprefix_ = child_.prefix
        elif nodeName_ == 'gst-amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'gst_amount')
            value_ = self.gds_validate_string(value_, node, 'gst_amount')
            self.gst_amount = value_
            self.gst_amount_nsprefix_ = child_.prefix
        elif nodeName_ == 'pst-amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pst_amount')
            value_ = self.gds_validate_string(value_, node, 'pst_amount')
            self.pst_amount = value_
            self.pst_amount_nsprefix_ = child_.prefix
        elif nodeName_ == 'hst-amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'hst_amount')
            value_ = self.gds_validate_string(value_, node, 'hst_amount')
            self.hst_amount = value_
            self.hst_amount_nsprefix_ = child_.prefix
        elif nodeName_ == 'priced-options':
            obj_ = priced_optionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.priced_options = obj_
            obj_.original_tagname_ = 'priced-options'
        elif nodeName_ == 'adjustments':
            obj_ = adjustmentsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.adjustments = obj_
            obj_.original_tagname_ = 'adjustments'
        elif nodeName_ == 'cc-receipt-details':
            obj_ = cc_receipt_detailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.cc_receipt_details = obj_
            obj_.original_tagname_ = 'cc-receipt-details'
        elif nodeName_ == 'service-standard':
            obj_ = service_standardType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.service_standard = obj_
            obj_.original_tagname_ = 'service-standard'
# end class NonContractShipmentReceiptType


class NonContractShipmentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, requested_shipping_point=None, delivery_spec=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.requested_shipping_point = requested_shipping_point
        self.requested_shipping_point_nsprefix_ = None
        self.delivery_spec = delivery_spec
        self.delivery_spec_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonContractShipmentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonContractShipmentType.subclass:
            return NonContractShipmentType.subclass(*args_, **kwargs_)
        else:
            return NonContractShipmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_requested_shipping_point(self):
        return self.requested_shipping_point
    def set_requested_shipping_point(self, requested_shipping_point):
        self.requested_shipping_point = requested_shipping_point
    def get_delivery_spec(self):
        return self.delivery_spec
    def set_delivery_spec(self, delivery_spec):
        self.delivery_spec = delivery_spec
    def _hasContent(self):
        if (
            self.requested_shipping_point is not None or
            self.delivery_spec is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonContractShipmentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonContractShipmentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonContractShipmentType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonContractShipmentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonContractShipmentType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.requested_shipping_point is not None:
            namespaceprefix_ = self.requested_shipping_point_nsprefix_ + ':' if (UseCapturedNS_ and self.requested_shipping_point_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srequested-shipping-point>%s</%srequested-shipping-point>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.requested_shipping_point), input_name='requested-shipping-point')), namespaceprefix_ , eol_))
        if self.delivery_spec is not None:
            namespaceprefix_ = self.delivery_spec_nsprefix_ + ':' if (UseCapturedNS_ and self.delivery_spec_nsprefix_) else ''
            self.delivery_spec.export(outfile, level, namespaceprefix_, namespacedef_='', name_='delivery-spec', pretty_print=pretty_print)
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
        if nodeName_ == 'requested-shipping-point':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'requested_shipping_point')
            value_ = self.gds_validate_string(value_, node, 'requested_shipping_point')
            self.requested_shipping_point = value_
            self.requested_shipping_point_nsprefix_ = child_.prefix
        elif nodeName_ == 'delivery-spec':
            obj_ = DeliverySpecType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.delivery_spec = obj_
            obj_.original_tagname_ = 'delivery-spec'
# end class NonContractShipmentType


class NonContractShipmentsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, link=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if link is None:
            self.link = []
        else:
            self.link = link
        self.link_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonContractShipmentsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonContractShipmentsType.subclass:
            return NonContractShipmentsType.subclass(*args_, **kwargs_)
        else:
            return NonContractShipmentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_link(self):
        return self.link
    def set_link(self, link):
        self.link = link
    def add_link(self, value):
        self.link.append(value)
    def insert_link_at(self, index, value):
        self.link.insert(index, value)
    def replace_link_at(self, index, value):
        self.link[index] = value
    def _hasContent(self):
        if (
            self.link
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonContractShipmentsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonContractShipmentsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonContractShipmentsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonContractShipmentsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonContractShipmentsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for link_ in self.link:
            namespaceprefix_ = self.link_nsprefix_ + ':' if (UseCapturedNS_ and self.link_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slink>%s</%slink>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(link_), input_name='link')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'link':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'link')
            value_ = self.gds_validate_string(value_, node, 'link')
            self.link.append(value_)
            self.link_nsprefix_ = child_.prefix
# end class NonContractShipmentsType


class DeliverySpecType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service_code=None, sender=None, destination=None, options=None, parcel_characteristics=None, notification=None, preferences=None, references=None, customs=None, settlement_info=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.service_code = service_code
        self.service_code_nsprefix_ = None
        self.sender = sender
        self.sender_nsprefix_ = None
        self.destination = destination
        self.destination_nsprefix_ = None
        self.options = options
        self.options_nsprefix_ = None
        self.parcel_characteristics = parcel_characteristics
        self.parcel_characteristics_nsprefix_ = None
        self.notification = notification
        self.notification_nsprefix_ = None
        self.preferences = preferences
        self.preferences_nsprefix_ = None
        self.references = references
        self.references_nsprefix_ = None
        self.customs = customs
        self.customs_nsprefix_ = None
        self.settlement_info = settlement_info
        self.settlement_info_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DeliverySpecType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DeliverySpecType.subclass:
            return DeliverySpecType.subclass(*args_, **kwargs_)
        else:
            return DeliverySpecType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_service_code(self):
        return self.service_code
    def set_service_code(self, service_code):
        self.service_code = service_code
    def get_sender(self):
        return self.sender
    def set_sender(self, sender):
        self.sender = sender
    def get_destination(self):
        return self.destination
    def set_destination(self, destination):
        self.destination = destination
    def get_options(self):
        return self.options
    def set_options(self, options):
        self.options = options
    def get_parcel_characteristics(self):
        return self.parcel_characteristics
    def set_parcel_characteristics(self, parcel_characteristics):
        self.parcel_characteristics = parcel_characteristics
    def get_notification(self):
        return self.notification
    def set_notification(self, notification):
        self.notification = notification
    def get_preferences(self):
        return self.preferences
    def set_preferences(self, preferences):
        self.preferences = preferences
    def get_references(self):
        return self.references
    def set_references(self, references):
        self.references = references
    def get_customs(self):
        return self.customs
    def set_customs(self, customs):
        self.customs = customs
    def get_settlement_info(self):
        return self.settlement_info
    def set_settlement_info(self, settlement_info):
        self.settlement_info = settlement_info
    def _hasContent(self):
        if (
            self.service_code is not None or
            self.sender is not None or
            self.destination is not None or
            self.options is not None or
            self.parcel_characteristics is not None or
            self.notification is not None or
            self.preferences is not None or
            self.references is not None or
            self.customs is not None or
            self.settlement_info is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DeliverySpecType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DeliverySpecType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DeliverySpecType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DeliverySpecType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DeliverySpecType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DeliverySpecType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DeliverySpecType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.service_code is not None:
            namespaceprefix_ = self.service_code_nsprefix_ + ':' if (UseCapturedNS_ and self.service_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-code>%s</%sservice-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_code), input_name='service-code')), namespaceprefix_ , eol_))
        if self.sender is not None:
            namespaceprefix_ = self.sender_nsprefix_ + ':' if (UseCapturedNS_ and self.sender_nsprefix_) else ''
            self.sender.export(outfile, level, namespaceprefix_, namespacedef_='', name_='sender', pretty_print=pretty_print)
        if self.destination is not None:
            namespaceprefix_ = self.destination_nsprefix_ + ':' if (UseCapturedNS_ and self.destination_nsprefix_) else ''
            self.destination.export(outfile, level, namespaceprefix_, namespacedef_='', name_='destination', pretty_print=pretty_print)
        if self.options is not None:
            namespaceprefix_ = self.options_nsprefix_ + ':' if (UseCapturedNS_ and self.options_nsprefix_) else ''
            self.options.export(outfile, level, namespaceprefix_, namespacedef_='', name_='options', pretty_print=pretty_print)
        if self.parcel_characteristics is not None:
            namespaceprefix_ = self.parcel_characteristics_nsprefix_ + ':' if (UseCapturedNS_ and self.parcel_characteristics_nsprefix_) else ''
            self.parcel_characteristics.export(outfile, level, namespaceprefix_, namespacedef_='', name_='parcel-characteristics', pretty_print=pretty_print)
        if self.notification is not None:
            namespaceprefix_ = self.notification_nsprefix_ + ':' if (UseCapturedNS_ and self.notification_nsprefix_) else ''
            self.notification.export(outfile, level, namespaceprefix_, namespacedef_='', name_='notification', pretty_print=pretty_print)
        if self.preferences is not None:
            namespaceprefix_ = self.preferences_nsprefix_ + ':' if (UseCapturedNS_ and self.preferences_nsprefix_) else ''
            self.preferences.export(outfile, level, namespaceprefix_, namespacedef_='', name_='preferences', pretty_print=pretty_print)
        if self.references is not None:
            namespaceprefix_ = self.references_nsprefix_ + ':' if (UseCapturedNS_ and self.references_nsprefix_) else ''
            self.references.export(outfile, level, namespaceprefix_, namespacedef_='', name_='references', pretty_print=pretty_print)
        if self.customs is not None:
            namespaceprefix_ = self.customs_nsprefix_ + ':' if (UseCapturedNS_ and self.customs_nsprefix_) else ''
            self.customs.export(outfile, level, namespaceprefix_, namespacedef_='', name_='customs', pretty_print=pretty_print)
        if self.settlement_info is not None:
            namespaceprefix_ = self.settlement_info_nsprefix_ + ':' if (UseCapturedNS_ and self.settlement_info_nsprefix_) else ''
            self.settlement_info.export(outfile, level, namespaceprefix_, namespacedef_='', name_='settlement-info', pretty_print=pretty_print)
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
        elif nodeName_ == 'sender':
            obj_ = SenderType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.sender = obj_
            obj_.original_tagname_ = 'sender'
        elif nodeName_ == 'destination':
            obj_ = DestinationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.destination = obj_
            obj_.original_tagname_ = 'destination'
        elif nodeName_ == 'options':
            obj_ = optionsType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.options = obj_
            obj_.original_tagname_ = 'options'
        elif nodeName_ == 'parcel-characteristics':
            obj_ = ParcelCharacteristicsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.parcel_characteristics = obj_
            obj_.original_tagname_ = 'parcel-characteristics'
        elif nodeName_ == 'notification':
            obj_ = NotificationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.notification = obj_
            obj_.original_tagname_ = 'notification'
        elif nodeName_ == 'preferences':
            obj_ = PreferencesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.preferences = obj_
            obj_.original_tagname_ = 'preferences'
        elif nodeName_ == 'references':
            obj_ = ReferencesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.references = obj_
            obj_.original_tagname_ = 'references'
        elif nodeName_ == 'customs':
            obj_ = CustomsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customs = obj_
            obj_.original_tagname_ = 'customs'
        elif nodeName_ == 'settlement-info':
            obj_ = SettlementInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.settlement_info = obj_
            obj_.original_tagname_ = 'settlement-info'
# end class DeliverySpecType


class CustomsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, currency=None, conversion_from_cad=None, reason_for_export=None, other_reason=None, sku_list=None, duties_and_taxes_prepaid=None, certificate_number=None, licence_number=None, invoice_number=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.currency = currency
        self.currency_nsprefix_ = None
        self.conversion_from_cad = conversion_from_cad
        self.validate_conversion_from_cadType(self.conversion_from_cad)
        self.conversion_from_cad_nsprefix_ = None
        self.reason_for_export = reason_for_export
        self.validate_reason_for_exportType(self.reason_for_export)
        self.reason_for_export_nsprefix_ = None
        self.other_reason = other_reason
        self.validate_other_reasonType(self.other_reason)
        self.other_reason_nsprefix_ = None
        self.sku_list = sku_list
        self.sku_list_nsprefix_ = None
        self.duties_and_taxes_prepaid = duties_and_taxes_prepaid
        self.validate_duties_and_taxes_prepaidType(self.duties_and_taxes_prepaid)
        self.duties_and_taxes_prepaid_nsprefix_ = None
        self.certificate_number = certificate_number
        self.validate_certificate_numberType(self.certificate_number)
        self.certificate_number_nsprefix_ = None
        self.licence_number = licence_number
        self.validate_licence_numberType(self.licence_number)
        self.licence_number_nsprefix_ = None
        self.invoice_number = invoice_number
        self.validate_invoice_numberType(self.invoice_number)
        self.invoice_number_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CustomsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CustomsType.subclass:
            return CustomsType.subclass(*args_, **kwargs_)
        else:
            return CustomsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_currency(self):
        return self.currency
    def set_currency(self, currency):
        self.currency = currency
    def get_conversion_from_cad(self):
        return self.conversion_from_cad
    def set_conversion_from_cad(self, conversion_from_cad):
        self.conversion_from_cad = conversion_from_cad
    def get_reason_for_export(self):
        return self.reason_for_export
    def set_reason_for_export(self, reason_for_export):
        self.reason_for_export = reason_for_export
    def get_other_reason(self):
        return self.other_reason
    def set_other_reason(self, other_reason):
        self.other_reason = other_reason
    def get_sku_list(self):
        return self.sku_list
    def set_sku_list(self, sku_list):
        self.sku_list = sku_list
    def get_duties_and_taxes_prepaid(self):
        return self.duties_and_taxes_prepaid
    def set_duties_and_taxes_prepaid(self, duties_and_taxes_prepaid):
        self.duties_and_taxes_prepaid = duties_and_taxes_prepaid
    def get_certificate_number(self):
        return self.certificate_number
    def set_certificate_number(self, certificate_number):
        self.certificate_number = certificate_number
    def get_licence_number(self):
        return self.licence_number
    def set_licence_number(self, licence_number):
        self.licence_number = licence_number
    def get_invoice_number(self):
        return self.invoice_number
    def set_invoice_number(self, invoice_number):
        self.invoice_number = invoice_number
    def validate_conversion_from_cadType(self, value):
        result = True
        # Validate type conversion-from-cadType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value > 999.999999:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on conversion-from-cadType' % {"value": value, "lineno": lineno} )
                result = False
            if value <= 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minExclusive restriction on conversion-from-cadType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_reason_for_exportType(self, value):
        result = True
        # Validate type reason-for-exportType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on reason-for-exportType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on reason-for-exportType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_other_reasonType(self, value):
        result = True
        # Validate type other-reasonType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on other-reasonType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_duties_and_taxes_prepaidType(self, value):
        result = True
        # Validate type duties-and-taxes-prepaidType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value > 99999.99:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on duties-and-taxes-prepaidType' % {"value": value, "lineno": lineno} )
                result = False
            if value <= 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minExclusive restriction on duties-and-taxes-prepaidType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_certificate_numberType(self, value):
        result = True
        # Validate type certificate-numberType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on certificate-numberType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_licence_numberType(self, value):
        result = True
        # Validate type licence-numberType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on licence-numberType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_invoice_numberType(self, value):
        result = True
        # Validate type invoice-numberType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on invoice-numberType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.currency is not None or
            self.conversion_from_cad is not None or
            self.reason_for_export is not None or
            self.other_reason is not None or
            self.sku_list is not None or
            self.duties_and_taxes_prepaid is not None or
            self.certificate_number is not None or
            self.licence_number is not None or
            self.invoice_number is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CustomsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CustomsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CustomsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CustomsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CustomsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CustomsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CustomsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.currency is not None:
            namespaceprefix_ = self.currency_nsprefix_ + ':' if (UseCapturedNS_ and self.currency_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scurrency>%s</%scurrency>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.currency), input_name='currency')), namespaceprefix_ , eol_))
        if self.conversion_from_cad is not None:
            namespaceprefix_ = self.conversion_from_cad_nsprefix_ + ':' if (UseCapturedNS_ and self.conversion_from_cad_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sconversion-from-cad>%s</%sconversion-from-cad>%s' % (namespaceprefix_ , self.gds_format_decimal(self.conversion_from_cad, input_name='conversion-from-cad'), namespaceprefix_ , eol_))
        if self.reason_for_export is not None:
            namespaceprefix_ = self.reason_for_export_nsprefix_ + ':' if (UseCapturedNS_ and self.reason_for_export_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreason-for-export>%s</%sreason-for-export>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.reason_for_export), input_name='reason-for-export')), namespaceprefix_ , eol_))
        if self.other_reason is not None:
            namespaceprefix_ = self.other_reason_nsprefix_ + ':' if (UseCapturedNS_ and self.other_reason_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sother-reason>%s</%sother-reason>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.other_reason), input_name='other-reason')), namespaceprefix_ , eol_))
        if self.sku_list is not None:
            namespaceprefix_ = self.sku_list_nsprefix_ + ':' if (UseCapturedNS_ and self.sku_list_nsprefix_) else ''
            self.sku_list.export(outfile, level, namespaceprefix_, namespacedef_='', name_='sku-list', pretty_print=pretty_print)
        if self.duties_and_taxes_prepaid is not None:
            namespaceprefix_ = self.duties_and_taxes_prepaid_nsprefix_ + ':' if (UseCapturedNS_ and self.duties_and_taxes_prepaid_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sduties-and-taxes-prepaid>%s</%sduties-and-taxes-prepaid>%s' % (namespaceprefix_ , self.gds_format_decimal(self.duties_and_taxes_prepaid, input_name='duties-and-taxes-prepaid'), namespaceprefix_ , eol_))
        if self.certificate_number is not None:
            namespaceprefix_ = self.certificate_number_nsprefix_ + ':' if (UseCapturedNS_ and self.certificate_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scertificate-number>%s</%scertificate-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.certificate_number), input_name='certificate-number')), namespaceprefix_ , eol_))
        if self.licence_number is not None:
            namespaceprefix_ = self.licence_number_nsprefix_ + ':' if (UseCapturedNS_ and self.licence_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slicence-number>%s</%slicence-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.licence_number), input_name='licence-number')), namespaceprefix_ , eol_))
        if self.invoice_number is not None:
            namespaceprefix_ = self.invoice_number_nsprefix_ + ':' if (UseCapturedNS_ and self.invoice_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinvoice-number>%s</%sinvoice-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.invoice_number), input_name='invoice-number')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'currency':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'currency')
            value_ = self.gds_validate_string(value_, node, 'currency')
            self.currency = value_
            self.currency_nsprefix_ = child_.prefix
        elif nodeName_ == 'conversion-from-cad' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'conversion_from_cad')
            fval_ = self.gds_validate_decimal(fval_, node, 'conversion_from_cad')
            self.conversion_from_cad = fval_
            self.conversion_from_cad_nsprefix_ = child_.prefix
            # validate type conversion-from-cadType
            self.validate_conversion_from_cadType(self.conversion_from_cad)
        elif nodeName_ == 'reason-for-export':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'reason_for_export')
            value_ = self.gds_validate_string(value_, node, 'reason_for_export')
            self.reason_for_export = value_
            self.reason_for_export_nsprefix_ = child_.prefix
            # validate type reason-for-exportType
            self.validate_reason_for_exportType(self.reason_for_export)
        elif nodeName_ == 'other-reason':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'other_reason')
            value_ = self.gds_validate_string(value_, node, 'other_reason')
            self.other_reason = value_
            self.other_reason_nsprefix_ = child_.prefix
            # validate type other-reasonType
            self.validate_other_reasonType(self.other_reason)
        elif nodeName_ == 'sku-list':
            obj_ = sku_listType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.sku_list = obj_
            obj_.original_tagname_ = 'sku-list'
        elif nodeName_ == 'duties-and-taxes-prepaid' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'duties_and_taxes_prepaid')
            fval_ = self.gds_validate_decimal(fval_, node, 'duties_and_taxes_prepaid')
            self.duties_and_taxes_prepaid = fval_
            self.duties_and_taxes_prepaid_nsprefix_ = child_.prefix
            # validate type duties-and-taxes-prepaidType
            self.validate_duties_and_taxes_prepaidType(self.duties_and_taxes_prepaid)
        elif nodeName_ == 'certificate-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'certificate_number')
            value_ = self.gds_validate_string(value_, node, 'certificate_number')
            self.certificate_number = value_
            self.certificate_number_nsprefix_ = child_.prefix
            # validate type certificate-numberType
            self.validate_certificate_numberType(self.certificate_number)
        elif nodeName_ == 'licence-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'licence_number')
            value_ = self.gds_validate_string(value_, node, 'licence_number')
            self.licence_number = value_
            self.licence_number_nsprefix_ = child_.prefix
            # validate type licence-numberType
            self.validate_licence_numberType(self.licence_number)
        elif nodeName_ == 'invoice-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'invoice_number')
            value_ = self.gds_validate_string(value_, node, 'invoice_number')
            self.invoice_number = value_
            self.invoice_number_nsprefix_ = child_.prefix
            # validate type invoice-numberType
            self.validate_invoice_numberType(self.invoice_number)
# end class CustomsType


class SkuType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, customs_number_of_units=None, customs_description=None, sku=None, hs_tariff_code=None, unit_weight=None, customs_value_per_unit=None, customs_unit_of_measure=None, country_of_origin=None, province_of_origin=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customs_number_of_units = customs_number_of_units
        self.validate_customs_number_of_unitsType(self.customs_number_of_units)
        self.customs_number_of_units_nsprefix_ = None
        self.customs_description = customs_description
        self.validate_customs_descriptionType(self.customs_description)
        self.customs_description_nsprefix_ = None
        self.sku = sku
        self.validate_skuType(self.sku)
        self.sku_nsprefix_ = None
        self.hs_tariff_code = hs_tariff_code
        self.validate_hs_tariff_codeType(self.hs_tariff_code)
        self.hs_tariff_code_nsprefix_ = None
        self.unit_weight = unit_weight
        self.validate_unit_weightType(self.unit_weight)
        self.unit_weight_nsprefix_ = None
        self.customs_value_per_unit = customs_value_per_unit
        self.validate_customs_value_per_unitType(self.customs_value_per_unit)
        self.customs_value_per_unit_nsprefix_ = None
        self.customs_unit_of_measure = customs_unit_of_measure
        self.customs_unit_of_measure_nsprefix_ = None
        self.country_of_origin = country_of_origin
        self.country_of_origin_nsprefix_ = None
        self.province_of_origin = province_of_origin
        self.province_of_origin_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SkuType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SkuType.subclass:
            return SkuType.subclass(*args_, **kwargs_)
        else:
            return SkuType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_customs_number_of_units(self):
        return self.customs_number_of_units
    def set_customs_number_of_units(self, customs_number_of_units):
        self.customs_number_of_units = customs_number_of_units
    def get_customs_description(self):
        return self.customs_description
    def set_customs_description(self, customs_description):
        self.customs_description = customs_description
    def get_sku(self):
        return self.sku
    def set_sku(self, sku):
        self.sku = sku
    def get_hs_tariff_code(self):
        return self.hs_tariff_code
    def set_hs_tariff_code(self, hs_tariff_code):
        self.hs_tariff_code = hs_tariff_code
    def get_unit_weight(self):
        return self.unit_weight
    def set_unit_weight(self, unit_weight):
        self.unit_weight = unit_weight
    def get_customs_value_per_unit(self):
        return self.customs_value_per_unit
    def set_customs_value_per_unit(self, customs_value_per_unit):
        self.customs_value_per_unit = customs_value_per_unit
    def get_customs_unit_of_measure(self):
        return self.customs_unit_of_measure
    def set_customs_unit_of_measure(self, customs_unit_of_measure):
        self.customs_unit_of_measure = customs_unit_of_measure
    def get_country_of_origin(self):
        return self.country_of_origin
    def set_country_of_origin(self, country_of_origin):
        self.country_of_origin = country_of_origin
    def get_province_of_origin(self):
        return self.province_of_origin
    def set_province_of_origin(self, province_of_origin):
        self.province_of_origin = province_of_origin
    def validate_customs_number_of_unitsType(self, value):
        result = True
        # Validate type customs-number-of-unitsType, a restriction on xsd:positiveInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on customs-number-of-unitsType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 9999:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on customs-number-of-unitsType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_customs_descriptionType(self, value):
        result = True
        # Validate type customs-descriptionType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 45:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on customs-descriptionType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on customs-descriptionType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_skuType(self, value):
        result = True
        # Validate type skuType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on skuType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_hs_tariff_codeType(self, value):
        result = True
        # Validate type hs-tariff-codeType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_hs_tariff_codeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_hs_tariff_codeType_patterns_, ))
                result = False
        return result
    validate_hs_tariff_codeType_patterns_ = [['^(\\d{4}(\\.\\d{2}(\\.\\d{2}(\\.\\d{2})?)?)?)$']]
    def validate_unit_weightType(self, value):
        result = True
        # Validate type unit-weightType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value > 99.999:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on unit-weightType' % {"value": value, "lineno": lineno} )
                result = False
            if value <= 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minExclusive restriction on unit-weightType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_customs_value_per_unitType(self, value):
        result = True
        # Validate type customs-value-per-unitType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value > 99999.99:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on customs-value-per-unitType' % {"value": value, "lineno": lineno} )
                result = False
            if value <= 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minExclusive restriction on customs-value-per-unitType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.customs_number_of_units is not None or
            self.customs_description is not None or
            self.sku is not None or
            self.hs_tariff_code is not None or
            self.unit_weight is not None or
            self.customs_value_per_unit is not None or
            self.customs_unit_of_measure is not None or
            self.country_of_origin is not None or
            self.province_of_origin is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SkuType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SkuType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SkuType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SkuType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SkuType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SkuType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SkuType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.customs_number_of_units is not None:
            namespaceprefix_ = self.customs_number_of_units_nsprefix_ + ':' if (UseCapturedNS_ and self.customs_number_of_units_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustoms-number-of-units>%s</%scustoms-number-of-units>%s' % (namespaceprefix_ , self.gds_format_integer(self.customs_number_of_units, input_name='customs-number-of-units'), namespaceprefix_ , eol_))
        if self.customs_description is not None:
            namespaceprefix_ = self.customs_description_nsprefix_ + ':' if (UseCapturedNS_ and self.customs_description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustoms-description>%s</%scustoms-description>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customs_description), input_name='customs-description')), namespaceprefix_ , eol_))
        if self.sku is not None:
            namespaceprefix_ = self.sku_nsprefix_ + ':' if (UseCapturedNS_ and self.sku_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssku>%s</%ssku>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.sku), input_name='sku')), namespaceprefix_ , eol_))
        if self.hs_tariff_code is not None:
            namespaceprefix_ = self.hs_tariff_code_nsprefix_ + ':' if (UseCapturedNS_ and self.hs_tariff_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shs-tariff-code>%s</%shs-tariff-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.hs_tariff_code), input_name='hs-tariff-code')), namespaceprefix_ , eol_))
        if self.unit_weight is not None:
            namespaceprefix_ = self.unit_weight_nsprefix_ + ':' if (UseCapturedNS_ and self.unit_weight_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunit-weight>%s</%sunit-weight>%s' % (namespaceprefix_ , self.gds_format_decimal(self.unit_weight, input_name='unit-weight'), namespaceprefix_ , eol_))
        if self.customs_value_per_unit is not None:
            namespaceprefix_ = self.customs_value_per_unit_nsprefix_ + ':' if (UseCapturedNS_ and self.customs_value_per_unit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustoms-value-per-unit>%s</%scustoms-value-per-unit>%s' % (namespaceprefix_ , self.gds_format_decimal(self.customs_value_per_unit, input_name='customs-value-per-unit'), namespaceprefix_ , eol_))
        if self.customs_unit_of_measure is not None:
            namespaceprefix_ = self.customs_unit_of_measure_nsprefix_ + ':' if (UseCapturedNS_ and self.customs_unit_of_measure_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustoms-unit-of-measure>%s</%scustoms-unit-of-measure>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customs_unit_of_measure), input_name='customs-unit-of-measure')), namespaceprefix_ , eol_))
        if self.country_of_origin is not None:
            namespaceprefix_ = self.country_of_origin_nsprefix_ + ':' if (UseCapturedNS_ and self.country_of_origin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountry-of-origin>%s</%scountry-of-origin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.country_of_origin), input_name='country-of-origin')), namespaceprefix_ , eol_))
        if self.province_of_origin is not None:
            namespaceprefix_ = self.province_of_origin_nsprefix_ + ':' if (UseCapturedNS_ and self.province_of_origin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprovince-of-origin>%s</%sprovince-of-origin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.province_of_origin), input_name='province-of-origin')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'customs-number-of-units' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'customs_number_of_units')
            if ival_ <= 0:
                raise_parse_error(child_, 'requires positiveInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'customs_number_of_units')
            self.customs_number_of_units = ival_
            self.customs_number_of_units_nsprefix_ = child_.prefix
            # validate type customs-number-of-unitsType
            self.validate_customs_number_of_unitsType(self.customs_number_of_units)
        elif nodeName_ == 'customs-description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customs_description')
            value_ = self.gds_validate_string(value_, node, 'customs_description')
            self.customs_description = value_
            self.customs_description_nsprefix_ = child_.prefix
            # validate type customs-descriptionType
            self.validate_customs_descriptionType(self.customs_description)
        elif nodeName_ == 'sku':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'sku')
            value_ = self.gds_validate_string(value_, node, 'sku')
            self.sku = value_
            self.sku_nsprefix_ = child_.prefix
            # validate type skuType
            self.validate_skuType(self.sku)
        elif nodeName_ == 'hs-tariff-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'hs_tariff_code')
            value_ = self.gds_validate_string(value_, node, 'hs_tariff_code')
            self.hs_tariff_code = value_
            self.hs_tariff_code_nsprefix_ = child_.prefix
            # validate type hs-tariff-codeType
            self.validate_hs_tariff_codeType(self.hs_tariff_code)
        elif nodeName_ == 'unit-weight' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'unit_weight')
            fval_ = self.gds_validate_decimal(fval_, node, 'unit_weight')
            self.unit_weight = fval_
            self.unit_weight_nsprefix_ = child_.prefix
            # validate type unit-weightType
            self.validate_unit_weightType(self.unit_weight)
        elif nodeName_ == 'customs-value-per-unit' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'customs_value_per_unit')
            fval_ = self.gds_validate_decimal(fval_, node, 'customs_value_per_unit')
            self.customs_value_per_unit = fval_
            self.customs_value_per_unit_nsprefix_ = child_.prefix
            # validate type customs-value-per-unitType
            self.validate_customs_value_per_unitType(self.customs_value_per_unit)
        elif nodeName_ == 'customs-unit-of-measure':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customs_unit_of_measure')
            value_ = self.gds_validate_string(value_, node, 'customs_unit_of_measure')
            self.customs_unit_of_measure = value_
            self.customs_unit_of_measure_nsprefix_ = child_.prefix
        elif nodeName_ == 'country-of-origin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'country_of_origin')
            value_ = self.gds_validate_string(value_, node, 'country_of_origin')
            self.country_of_origin = value_
            self.country_of_origin_nsprefix_ = child_.prefix
        elif nodeName_ == 'province-of-origin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'province_of_origin')
            value_ = self.gds_validate_string(value_, node, 'province_of_origin')
            self.province_of_origin = value_
            self.province_of_origin_nsprefix_ = child_.prefix
# end class SkuType


class SenderType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, company=None, contact_phone=None, address_details=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.validate_ContactNameType(self.name)
        self.name_nsprefix_ = None
        self.company = company
        self.validate_CompanyNameType(self.company)
        self.company_nsprefix_ = None
        self.contact_phone = contact_phone
        self.contact_phone_nsprefix_ = None
        self.address_details = address_details
        self.address_details_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SenderType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SenderType.subclass:
            return SenderType.subclass(*args_, **kwargs_)
        else:
            return SenderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_company(self):
        return self.company
    def set_company(self, company):
        self.company = company
    def get_contact_phone(self):
        return self.contact_phone
    def set_contact_phone(self, contact_phone):
        self.contact_phone = contact_phone
    def get_address_details(self):
        return self.address_details
    def set_address_details(self, address_details):
        self.address_details = address_details
    def validate_ContactNameType(self, value):
        result = True
        # Validate type ContactNameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ContactNameType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_CompanyNameType(self, value):
        result = True
        # Validate type CompanyNameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CompanyNameType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.name is not None or
            self.company is not None or
            self.contact_phone is not None or
            self.address_details is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SenderType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SenderType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SenderType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SenderType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SenderType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SenderType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SenderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.name), input_name='name')), namespaceprefix_ , eol_))
        if self.company is not None:
            namespaceprefix_ = self.company_nsprefix_ + ':' if (UseCapturedNS_ and self.company_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scompany>%s</%scompany>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.company), input_name='company')), namespaceprefix_ , eol_))
        if self.contact_phone is not None:
            namespaceprefix_ = self.contact_phone_nsprefix_ + ':' if (UseCapturedNS_ and self.contact_phone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontact-phone>%s</%scontact-phone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contact_phone), input_name='contact-phone')), namespaceprefix_ , eol_))
        if self.address_details is not None:
            namespaceprefix_ = self.address_details_nsprefix_ + ':' if (UseCapturedNS_ and self.address_details_nsprefix_) else ''
            self.address_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='address-details', pretty_print=pretty_print)
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
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type ContactNameType
            self.validate_ContactNameType(self.name)
        elif nodeName_ == 'company':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'company')
            value_ = self.gds_validate_string(value_, node, 'company')
            self.company = value_
            self.company_nsprefix_ = child_.prefix
            # validate type CompanyNameType
            self.validate_CompanyNameType(self.company)
        elif nodeName_ == 'contact-phone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contact_phone')
            value_ = self.gds_validate_string(value_, node, 'contact_phone')
            self.contact_phone = value_
            self.contact_phone_nsprefix_ = child_.prefix
        elif nodeName_ == 'address-details':
            obj_ = DomesticAddressDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address_details = obj_
            obj_.original_tagname_ = 'address-details'
# end class SenderType


class RecipientAddressType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, company=None, additional_address_info=None, client_voice_number=None, address_details=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.validate_ContactNameType(self.name)
        self.name_nsprefix_ = None
        self.company = company
        self.validate_CompanyNameType(self.company)
        self.company_nsprefix_ = None
        self.additional_address_info = additional_address_info
        self.validate_additional_address_infoType(self.additional_address_info)
        self.additional_address_info_nsprefix_ = None
        self.client_voice_number = client_voice_number
        self.client_voice_number_nsprefix_ = None
        self.address_details = address_details
        self.address_details_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RecipientAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RecipientAddressType.subclass:
            return RecipientAddressType.subclass(*args_, **kwargs_)
        else:
            return RecipientAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_company(self):
        return self.company
    def set_company(self, company):
        self.company = company
    def get_additional_address_info(self):
        return self.additional_address_info
    def set_additional_address_info(self, additional_address_info):
        self.additional_address_info = additional_address_info
    def get_client_voice_number(self):
        return self.client_voice_number
    def set_client_voice_number(self, client_voice_number):
        self.client_voice_number = client_voice_number
    def get_address_details(self):
        return self.address_details
    def set_address_details(self, address_details):
        self.address_details = address_details
    def validate_ContactNameType(self, value):
        result = True
        # Validate type ContactNameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ContactNameType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_CompanyNameType(self, value):
        result = True
        # Validate type CompanyNameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CompanyNameType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_additional_address_infoType(self, value):
        result = True
        # Validate type additional-address-infoType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on additional-address-infoType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.name is not None or
            self.company is not None or
            self.additional_address_info is not None or
            self.client_voice_number is not None or
            self.address_details is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RecipientAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RecipientAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RecipientAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RecipientAddressType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RecipientAddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RecipientAddressType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RecipientAddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.name), input_name='name')), namespaceprefix_ , eol_))
        if self.company is not None:
            namespaceprefix_ = self.company_nsprefix_ + ':' if (UseCapturedNS_ and self.company_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scompany>%s</%scompany>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.company), input_name='company')), namespaceprefix_ , eol_))
        if self.additional_address_info is not None:
            namespaceprefix_ = self.additional_address_info_nsprefix_ + ':' if (UseCapturedNS_ and self.additional_address_info_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadditional-address-info>%s</%sadditional-address-info>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.additional_address_info), input_name='additional-address-info')), namespaceprefix_ , eol_))
        if self.client_voice_number is not None:
            namespaceprefix_ = self.client_voice_number_nsprefix_ + ':' if (UseCapturedNS_ and self.client_voice_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sclient-voice-number>%s</%sclient-voice-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.client_voice_number), input_name='client-voice-number')), namespaceprefix_ , eol_))
        if self.address_details is not None:
            namespaceprefix_ = self.address_details_nsprefix_ + ':' if (UseCapturedNS_ and self.address_details_nsprefix_) else ''
            self.address_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='address-details', pretty_print=pretty_print)
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
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type ContactNameType
            self.validate_ContactNameType(self.name)
        elif nodeName_ == 'company':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'company')
            value_ = self.gds_validate_string(value_, node, 'company')
            self.company = value_
            self.company_nsprefix_ = child_.prefix
            # validate type CompanyNameType
            self.validate_CompanyNameType(self.company)
        elif nodeName_ == 'additional-address-info':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'additional_address_info')
            value_ = self.gds_validate_string(value_, node, 'additional_address_info')
            self.additional_address_info = value_
            self.additional_address_info_nsprefix_ = child_.prefix
            # validate type additional-address-infoType
            self.validate_additional_address_infoType(self.additional_address_info)
        elif nodeName_ == 'client-voice-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'client_voice_number')
            value_ = self.gds_validate_string(value_, node, 'client_voice_number')
            self.client_voice_number = value_
            self.client_voice_number_nsprefix_ = child_.prefix
        elif nodeName_ == 'address-details':
            obj_ = DestinationAddressDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address_details = obj_
            obj_.original_tagname_ = 'address-details'
# end class RecipientAddressType


class DestinationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, company=None, additional_address_info=None, client_voice_number=None, address_details=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.validate_ContactNameType(self.name)
        self.name_nsprefix_ = None
        self.company = company
        self.validate_CompanyNameType(self.company)
        self.company_nsprefix_ = None
        self.additional_address_info = additional_address_info
        self.validate_additional_address_infoType2(self.additional_address_info)
        self.additional_address_info_nsprefix_ = None
        self.client_voice_number = client_voice_number
        self.client_voice_number_nsprefix_ = None
        self.address_details = address_details
        self.address_details_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DestinationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DestinationType.subclass:
            return DestinationType.subclass(*args_, **kwargs_)
        else:
            return DestinationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_company(self):
        return self.company
    def set_company(self, company):
        self.company = company
    def get_additional_address_info(self):
        return self.additional_address_info
    def set_additional_address_info(self, additional_address_info):
        self.additional_address_info = additional_address_info
    def get_client_voice_number(self):
        return self.client_voice_number
    def set_client_voice_number(self, client_voice_number):
        self.client_voice_number = client_voice_number
    def get_address_details(self):
        return self.address_details
    def set_address_details(self, address_details):
        self.address_details = address_details
    def validate_ContactNameType(self, value):
        result = True
        # Validate type ContactNameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ContactNameType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_CompanyNameType(self, value):
        result = True
        # Validate type CompanyNameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CompanyNameType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_additional_address_infoType2(self, value):
        result = True
        # Validate type additional-address-infoType2, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on additional-address-infoType2' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.name is not None or
            self.company is not None or
            self.additional_address_info is not None or
            self.client_voice_number is not None or
            self.address_details is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DestinationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DestinationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DestinationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DestinationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DestinationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DestinationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DestinationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.name), input_name='name')), namespaceprefix_ , eol_))
        if self.company is not None:
            namespaceprefix_ = self.company_nsprefix_ + ':' if (UseCapturedNS_ and self.company_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scompany>%s</%scompany>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.company), input_name='company')), namespaceprefix_ , eol_))
        if self.additional_address_info is not None:
            namespaceprefix_ = self.additional_address_info_nsprefix_ + ':' if (UseCapturedNS_ and self.additional_address_info_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadditional-address-info>%s</%sadditional-address-info>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.additional_address_info), input_name='additional-address-info')), namespaceprefix_ , eol_))
        if self.client_voice_number is not None:
            namespaceprefix_ = self.client_voice_number_nsprefix_ + ':' if (UseCapturedNS_ and self.client_voice_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sclient-voice-number>%s</%sclient-voice-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.client_voice_number), input_name='client-voice-number')), namespaceprefix_ , eol_))
        if self.address_details is not None:
            namespaceprefix_ = self.address_details_nsprefix_ + ':' if (UseCapturedNS_ and self.address_details_nsprefix_) else ''
            self.address_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='address-details', pretty_print=pretty_print)
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
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type ContactNameType
            self.validate_ContactNameType(self.name)
        elif nodeName_ == 'company':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'company')
            value_ = self.gds_validate_string(value_, node, 'company')
            self.company = value_
            self.company_nsprefix_ = child_.prefix
            # validate type CompanyNameType
            self.validate_CompanyNameType(self.company)
        elif nodeName_ == 'additional-address-info':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'additional_address_info')
            value_ = self.gds_validate_string(value_, node, 'additional_address_info')
            self.additional_address_info = value_
            self.additional_address_info_nsprefix_ = child_.prefix
            # validate type additional-address-infoType2
            self.validate_additional_address_infoType2(self.additional_address_info)
        elif nodeName_ == 'client-voice-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'client_voice_number')
            value_ = self.gds_validate_string(value_, node, 'client_voice_number')
            self.client_voice_number = value_
            self.client_voice_number_nsprefix_ = child_.prefix
        elif nodeName_ == 'address-details':
            obj_ = DestinationAddressDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address_details = obj_
            obj_.original_tagname_ = 'address-details'
# end class DestinationType


class DomesticAddressDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, address_line_1=None, address_line_2=None, city=None, prov_state=None, postal_zip_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.address_line_1 = address_line_1
        self.validate_address_line_1Type(self.address_line_1)
        self.address_line_1_nsprefix_ = None
        self.address_line_2 = address_line_2
        self.validate_address_line_2Type(self.address_line_2)
        self.address_line_2_nsprefix_ = None
        self.city = city
        self.validate_cityType(self.city)
        self.city_nsprefix_ = None
        self.prov_state = prov_state
        self.prov_state_nsprefix_ = None
        self.postal_zip_code = postal_zip_code
        self.postal_zip_code_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DomesticAddressDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DomesticAddressDetailsType.subclass:
            return DomesticAddressDetailsType.subclass(*args_, **kwargs_)
        else:
            return DomesticAddressDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_address_line_1(self):
        return self.address_line_1
    def set_address_line_1(self, address_line_1):
        self.address_line_1 = address_line_1
    def get_address_line_2(self):
        return self.address_line_2
    def set_address_line_2(self, address_line_2):
        self.address_line_2 = address_line_2
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_prov_state(self):
        return self.prov_state
    def set_prov_state(self, prov_state):
        self.prov_state = prov_state
    def get_postal_zip_code(self):
        return self.postal_zip_code
    def set_postal_zip_code(self, postal_zip_code):
        self.postal_zip_code = postal_zip_code
    def validate_address_line_1Type(self, value):
        result = True
        # Validate type address-line-1Type, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on address-line-1Type' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on address-line-1Type' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_address_line_2Type(self, value):
        result = True
        # Validate type address-line-2Type, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on address-line-2Type' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_cityType(self, value):
        result = True
        # Validate type cityType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on cityType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on cityType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.address_line_1 is not None or
            self.address_line_2 is not None or
            self.city is not None or
            self.prov_state is not None or
            self.postal_zip_code is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DomesticAddressDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DomesticAddressDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DomesticAddressDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DomesticAddressDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DomesticAddressDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DomesticAddressDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DomesticAddressDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.address_line_1 is not None:
            namespaceprefix_ = self.address_line_1_nsprefix_ + ':' if (UseCapturedNS_ and self.address_line_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddress-line-1>%s</%saddress-line-1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.address_line_1), input_name='address-line-1')), namespaceprefix_ , eol_))
        if self.address_line_2 is not None:
            namespaceprefix_ = self.address_line_2_nsprefix_ + ':' if (UseCapturedNS_ and self.address_line_2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddress-line-2>%s</%saddress-line-2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.address_line_2), input_name='address-line-2')), namespaceprefix_ , eol_))
        if self.city is not None:
            namespaceprefix_ = self.city_nsprefix_ + ':' if (UseCapturedNS_ and self.city_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scity>%s</%scity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.city), input_name='city')), namespaceprefix_ , eol_))
        if self.prov_state is not None:
            namespaceprefix_ = self.prov_state_nsprefix_ + ':' if (UseCapturedNS_ and self.prov_state_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprov-state>%s</%sprov-state>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.prov_state), input_name='prov-state')), namespaceprefix_ , eol_))
        if self.postal_zip_code is not None:
            namespaceprefix_ = self.postal_zip_code_nsprefix_ + ':' if (UseCapturedNS_ and self.postal_zip_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostal-zip-code>%s</%spostal-zip-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.postal_zip_code), input_name='postal-zip-code')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'address-line-1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'address_line_1')
            value_ = self.gds_validate_string(value_, node, 'address_line_1')
            self.address_line_1 = value_
            self.address_line_1_nsprefix_ = child_.prefix
            # validate type address-line-1Type
            self.validate_address_line_1Type(self.address_line_1)
        elif nodeName_ == 'address-line-2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'address_line_2')
            value_ = self.gds_validate_string(value_, node, 'address_line_2')
            self.address_line_2 = value_
            self.address_line_2_nsprefix_ = child_.prefix
            # validate type address-line-2Type
            self.validate_address_line_2Type(self.address_line_2)
        elif nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type cityType
            self.validate_cityType(self.city)
        elif nodeName_ == 'prov-state':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'prov_state')
            value_ = self.gds_validate_string(value_, node, 'prov_state')
            self.prov_state = value_
            self.prov_state_nsprefix_ = child_.prefix
        elif nodeName_ == 'postal-zip-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postal_zip_code')
            value_ = self.gds_validate_string(value_, node, 'postal_zip_code')
            self.postal_zip_code = value_
            self.postal_zip_code_nsprefix_ = child_.prefix
# end class DomesticAddressDetailsType


class AddressDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, address_line_1=None, address_line_2=None, city=None, prov_state=None, country_code=None, postal_zip_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.address_line_1 = address_line_1
        self.validate_address_line_1Type3(self.address_line_1)
        self.address_line_1_nsprefix_ = None
        self.address_line_2 = address_line_2
        self.validate_address_line_2Type4(self.address_line_2)
        self.address_line_2_nsprefix_ = None
        self.city = city
        self.validate_cityType5(self.city)
        self.city_nsprefix_ = None
        self.prov_state = prov_state
        self.prov_state_nsprefix_ = None
        self.country_code = country_code
        self.country_code_nsprefix_ = None
        self.postal_zip_code = postal_zip_code
        self.postal_zip_code_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AddressDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AddressDetailsType.subclass:
            return AddressDetailsType.subclass(*args_, **kwargs_)
        else:
            return AddressDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_address_line_1(self):
        return self.address_line_1
    def set_address_line_1(self, address_line_1):
        self.address_line_1 = address_line_1
    def get_address_line_2(self):
        return self.address_line_2
    def set_address_line_2(self, address_line_2):
        self.address_line_2 = address_line_2
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_prov_state(self):
        return self.prov_state
    def set_prov_state(self, prov_state):
        self.prov_state = prov_state
    def get_country_code(self):
        return self.country_code
    def set_country_code(self, country_code):
        self.country_code = country_code
    def get_postal_zip_code(self):
        return self.postal_zip_code
    def set_postal_zip_code(self, postal_zip_code):
        self.postal_zip_code = postal_zip_code
    def validate_address_line_1Type3(self, value):
        result = True
        # Validate type address-line-1Type3, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on address-line-1Type3' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on address-line-1Type3' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_address_line_2Type4(self, value):
        result = True
        # Validate type address-line-2Type4, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on address-line-2Type4' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_cityType5(self, value):
        result = True
        # Validate type cityType5, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on cityType5' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on cityType5' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.address_line_1 is not None or
            self.address_line_2 is not None or
            self.city is not None or
            self.prov_state is not None or
            self.country_code is not None or
            self.postal_zip_code is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AddressDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AddressDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AddressDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AddressDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AddressDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AddressDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AddressDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.address_line_1 is not None:
            namespaceprefix_ = self.address_line_1_nsprefix_ + ':' if (UseCapturedNS_ and self.address_line_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddress-line-1>%s</%saddress-line-1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.address_line_1), input_name='address-line-1')), namespaceprefix_ , eol_))
        if self.address_line_2 is not None:
            namespaceprefix_ = self.address_line_2_nsprefix_ + ':' if (UseCapturedNS_ and self.address_line_2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddress-line-2>%s</%saddress-line-2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.address_line_2), input_name='address-line-2')), namespaceprefix_ , eol_))
        if self.city is not None:
            namespaceprefix_ = self.city_nsprefix_ + ':' if (UseCapturedNS_ and self.city_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scity>%s</%scity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.city), input_name='city')), namespaceprefix_ , eol_))
        if self.prov_state is not None:
            namespaceprefix_ = self.prov_state_nsprefix_ + ':' if (UseCapturedNS_ and self.prov_state_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprov-state>%s</%sprov-state>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.prov_state), input_name='prov-state')), namespaceprefix_ , eol_))
        if self.country_code is not None:
            namespaceprefix_ = self.country_code_nsprefix_ + ':' if (UseCapturedNS_ and self.country_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountry-code>%s</%scountry-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.country_code), input_name='country-code')), namespaceprefix_ , eol_))
        if self.postal_zip_code is not None:
            namespaceprefix_ = self.postal_zip_code_nsprefix_ + ':' if (UseCapturedNS_ and self.postal_zip_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostal-zip-code>%s</%spostal-zip-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.postal_zip_code), input_name='postal-zip-code')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'address-line-1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'address_line_1')
            value_ = self.gds_validate_string(value_, node, 'address_line_1')
            self.address_line_1 = value_
            self.address_line_1_nsprefix_ = child_.prefix
            # validate type address-line-1Type3
            self.validate_address_line_1Type3(self.address_line_1)
        elif nodeName_ == 'address-line-2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'address_line_2')
            value_ = self.gds_validate_string(value_, node, 'address_line_2')
            self.address_line_2 = value_
            self.address_line_2_nsprefix_ = child_.prefix
            # validate type address-line-2Type4
            self.validate_address_line_2Type4(self.address_line_2)
        elif nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type cityType5
            self.validate_cityType5(self.city)
        elif nodeName_ == 'prov-state':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'prov_state')
            value_ = self.gds_validate_string(value_, node, 'prov_state')
            self.prov_state = value_
            self.prov_state_nsprefix_ = child_.prefix
        elif nodeName_ == 'country-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'country_code')
            value_ = self.gds_validate_string(value_, node, 'country_code')
            self.country_code = value_
            self.country_code_nsprefix_ = child_.prefix
        elif nodeName_ == 'postal-zip-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postal_zip_code')
            value_ = self.gds_validate_string(value_, node, 'postal_zip_code')
            self.postal_zip_code = value_
            self.postal_zip_code_nsprefix_ = child_.prefix
# end class AddressDetailsType


class DestinationAddressDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, address_line_1=None, address_line_2=None, city=None, prov_state=None, country_code=None, postal_zip_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.address_line_1 = address_line_1
        self.validate_address_line_1Type6(self.address_line_1)
        self.address_line_1_nsprefix_ = None
        self.address_line_2 = address_line_2
        self.validate_address_line_2Type7(self.address_line_2)
        self.address_line_2_nsprefix_ = None
        self.city = city
        self.validate_cityType8(self.city)
        self.city_nsprefix_ = None
        self.prov_state = prov_state
        self.prov_state_nsprefix_ = None
        self.country_code = country_code
        self.country_code_nsprefix_ = None
        self.postal_zip_code = postal_zip_code
        self.postal_zip_code_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DestinationAddressDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DestinationAddressDetailsType.subclass:
            return DestinationAddressDetailsType.subclass(*args_, **kwargs_)
        else:
            return DestinationAddressDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_address_line_1(self):
        return self.address_line_1
    def set_address_line_1(self, address_line_1):
        self.address_line_1 = address_line_1
    def get_address_line_2(self):
        return self.address_line_2
    def set_address_line_2(self, address_line_2):
        self.address_line_2 = address_line_2
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_prov_state(self):
        return self.prov_state
    def set_prov_state(self, prov_state):
        self.prov_state = prov_state
    def get_country_code(self):
        return self.country_code
    def set_country_code(self, country_code):
        self.country_code = country_code
    def get_postal_zip_code(self):
        return self.postal_zip_code
    def set_postal_zip_code(self, postal_zip_code):
        self.postal_zip_code = postal_zip_code
    def validate_address_line_1Type6(self, value):
        result = True
        # Validate type address-line-1Type6, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on address-line-1Type6' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on address-line-1Type6' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_address_line_2Type7(self, value):
        result = True
        # Validate type address-line-2Type7, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on address-line-2Type7' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_cityType8(self, value):
        result = True
        # Validate type cityType8, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on cityType8' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on cityType8' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.address_line_1 is not None or
            self.address_line_2 is not None or
            self.city is not None or
            self.prov_state is not None or
            self.country_code is not None or
            self.postal_zip_code is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DestinationAddressDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DestinationAddressDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DestinationAddressDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DestinationAddressDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DestinationAddressDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DestinationAddressDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DestinationAddressDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.address_line_1 is not None:
            namespaceprefix_ = self.address_line_1_nsprefix_ + ':' if (UseCapturedNS_ and self.address_line_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddress-line-1>%s</%saddress-line-1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.address_line_1), input_name='address-line-1')), namespaceprefix_ , eol_))
        if self.address_line_2 is not None:
            namespaceprefix_ = self.address_line_2_nsprefix_ + ':' if (UseCapturedNS_ and self.address_line_2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddress-line-2>%s</%saddress-line-2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.address_line_2), input_name='address-line-2')), namespaceprefix_ , eol_))
        if self.city is not None:
            namespaceprefix_ = self.city_nsprefix_ + ':' if (UseCapturedNS_ and self.city_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scity>%s</%scity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.city), input_name='city')), namespaceprefix_ , eol_))
        if self.prov_state is not None:
            namespaceprefix_ = self.prov_state_nsprefix_ + ':' if (UseCapturedNS_ and self.prov_state_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprov-state>%s</%sprov-state>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.prov_state), input_name='prov-state')), namespaceprefix_ , eol_))
        if self.country_code is not None:
            namespaceprefix_ = self.country_code_nsprefix_ + ':' if (UseCapturedNS_ and self.country_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountry-code>%s</%scountry-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.country_code), input_name='country-code')), namespaceprefix_ , eol_))
        if self.postal_zip_code is not None:
            namespaceprefix_ = self.postal_zip_code_nsprefix_ + ':' if (UseCapturedNS_ and self.postal_zip_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostal-zip-code>%s</%spostal-zip-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.postal_zip_code), input_name='postal-zip-code')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'address-line-1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'address_line_1')
            value_ = self.gds_validate_string(value_, node, 'address_line_1')
            self.address_line_1 = value_
            self.address_line_1_nsprefix_ = child_.prefix
            # validate type address-line-1Type6
            self.validate_address_line_1Type6(self.address_line_1)
        elif nodeName_ == 'address-line-2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'address_line_2')
            value_ = self.gds_validate_string(value_, node, 'address_line_2')
            self.address_line_2 = value_
            self.address_line_2_nsprefix_ = child_.prefix
            # validate type address-line-2Type7
            self.validate_address_line_2Type7(self.address_line_2)
        elif nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type cityType8
            self.validate_cityType8(self.city)
        elif nodeName_ == 'prov-state':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'prov_state')
            value_ = self.gds_validate_string(value_, node, 'prov_state')
            self.prov_state = value_
            self.prov_state_nsprefix_ = child_.prefix
        elif nodeName_ == 'country-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'country_code')
            value_ = self.gds_validate_string(value_, node, 'country_code')
            self.country_code = value_
            self.country_code_nsprefix_ = child_.prefix
        elif nodeName_ == 'postal-zip-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postal_zip_code')
            value_ = self.gds_validate_string(value_, node, 'postal_zip_code')
            self.postal_zip_code = value_
            self.postal_zip_code_nsprefix_ = child_.prefix
# end class DestinationAddressDetailsType


class OptionType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, option_code=None, option_amount=None, option_qualifier_1=None, option_qualifier_2=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.option_code = option_code
        self.validate_option_codeType9(self.option_code)
        self.option_code_nsprefix_ = None
        self.option_amount = option_amount
        self.option_amount_nsprefix_ = None
        self.option_qualifier_1 = option_qualifier_1
        self.option_qualifier_1_nsprefix_ = None
        self.option_qualifier_2 = option_qualifier_2
        self.validate_option_qualifier_2Type(self.option_qualifier_2)
        self.option_qualifier_2_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OptionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OptionType.subclass:
            return OptionType.subclass(*args_, **kwargs_)
        else:
            return OptionType(*args_, **kwargs_)
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
    def get_option_qualifier_1(self):
        return self.option_qualifier_1
    def set_option_qualifier_1(self, option_qualifier_1):
        self.option_qualifier_1 = option_qualifier_1
    def get_option_qualifier_2(self):
        return self.option_qualifier_2
    def set_option_qualifier_2(self, option_qualifier_2):
        self.option_qualifier_2 = option_qualifier_2
    def validate_option_codeType9(self, value):
        result = True
        # Validate type option-codeType9, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on option-codeType9' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on option-codeType9' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_option_qualifier_2Type(self, value):
        result = True
        # Validate type option-qualifier-2Type, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on option-qualifier-2Type' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.option_code is not None or
            self.option_amount is not None or
            self.option_qualifier_1 is not None or
            self.option_qualifier_2 is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='OptionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OptionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OptionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OptionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OptionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OptionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='OptionType', fromsubclass_=False, pretty_print=True):
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
        if self.option_qualifier_1 is not None:
            namespaceprefix_ = self.option_qualifier_1_nsprefix_ + ':' if (UseCapturedNS_ and self.option_qualifier_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-qualifier-1>%s</%soption-qualifier-1>%s' % (namespaceprefix_ , self.gds_format_boolean(self.option_qualifier_1, input_name='option-qualifier-1'), namespaceprefix_ , eol_))
        if self.option_qualifier_2 is not None:
            namespaceprefix_ = self.option_qualifier_2_nsprefix_ + ':' if (UseCapturedNS_ and self.option_qualifier_2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-qualifier-2>%s</%soption-qualifier-2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.option_qualifier_2), input_name='option-qualifier-2')), namespaceprefix_ , eol_))
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
            # validate type option-codeType9
            self.validate_option_codeType9(self.option_code)
        elif nodeName_ == 'option-amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'option_amount')
            value_ = self.gds_validate_string(value_, node, 'option_amount')
            self.option_amount = value_
            self.option_amount_nsprefix_ = child_.prefix
        elif nodeName_ == 'option-qualifier-1':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'option_qualifier_1')
            ival_ = self.gds_validate_boolean(ival_, node, 'option_qualifier_1')
            self.option_qualifier_1 = ival_
            self.option_qualifier_1_nsprefix_ = child_.prefix
        elif nodeName_ == 'option-qualifier-2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'option_qualifier_2')
            value_ = self.gds_validate_string(value_, node, 'option_qualifier_2')
            self.option_qualifier_2 = value_
            self.option_qualifier_2_nsprefix_ = child_.prefix
            # validate type option-qualifier-2Type
            self.validate_option_qualifier_2Type(self.option_qualifier_2)
# end class OptionType


class ParcelCharacteristicsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, weight=None, dimensions=None, document=None, unpackaged=None, mailing_tube=None, gds_collector_=None, **kwargs_):
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
        self.document = document
        self.document_nsprefix_ = None
        self.unpackaged = unpackaged
        self.unpackaged_nsprefix_ = None
        self.mailing_tube = mailing_tube
        self.mailing_tube_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParcelCharacteristicsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParcelCharacteristicsType.subclass:
            return ParcelCharacteristicsType.subclass(*args_, **kwargs_)
        else:
            return ParcelCharacteristicsType(*args_, **kwargs_)
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
    def get_document(self):
        return self.document
    def set_document(self, document):
        self.document = document
    def get_unpackaged(self):
        return self.unpackaged
    def set_unpackaged(self, unpackaged):
        self.unpackaged = unpackaged
    def get_mailing_tube(self):
        return self.mailing_tube
    def set_mailing_tube(self, mailing_tube):
        self.mailing_tube = mailing_tube
    def validate_weightType(self, value):
        result = True
        # Validate type weightType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value > 999.999:
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
            self.document is not None or
            self.unpackaged is not None or
            self.mailing_tube is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ParcelCharacteristicsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParcelCharacteristicsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParcelCharacteristicsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParcelCharacteristicsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParcelCharacteristicsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParcelCharacteristicsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ParcelCharacteristicsType', fromsubclass_=False, pretty_print=True):
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
        if self.document is not None:
            namespaceprefix_ = self.document_nsprefix_ + ':' if (UseCapturedNS_ and self.document_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdocument>%s</%sdocument>%s' % (namespaceprefix_ , self.gds_format_boolean(self.document, input_name='document'), namespaceprefix_ , eol_))
        if self.unpackaged is not None:
            namespaceprefix_ = self.unpackaged_nsprefix_ + ':' if (UseCapturedNS_ and self.unpackaged_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunpackaged>%s</%sunpackaged>%s' % (namespaceprefix_ , self.gds_format_boolean(self.unpackaged, input_name='unpackaged'), namespaceprefix_ , eol_))
        if self.mailing_tube is not None:
            namespaceprefix_ = self.mailing_tube_nsprefix_ + ':' if (UseCapturedNS_ and self.mailing_tube_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smailing-tube>%s</%smailing-tube>%s' % (namespaceprefix_ , self.gds_format_boolean(self.mailing_tube, input_name='mailing-tube'), namespaceprefix_ , eol_))
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
        elif nodeName_ == 'document':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'document')
            ival_ = self.gds_validate_boolean(ival_, node, 'document')
            self.document = ival_
            self.document_nsprefix_ = child_.prefix
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
# end class ParcelCharacteristicsType


class NotificationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, email=None, on_shipment=None, on_exception=None, on_delivery=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.email = email
        self.validate_EmailType(self.email)
        self.email_nsprefix_ = None
        self.on_shipment = on_shipment
        self.on_shipment_nsprefix_ = None
        self.on_exception = on_exception
        self.on_exception_nsprefix_ = None
        self.on_delivery = on_delivery
        self.on_delivery_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NotificationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NotificationType.subclass:
            return NotificationType.subclass(*args_, **kwargs_)
        else:
            return NotificationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def get_on_shipment(self):
        return self.on_shipment
    def set_on_shipment(self, on_shipment):
        self.on_shipment = on_shipment
    def get_on_exception(self):
        return self.on_exception
    def set_on_exception(self, on_exception):
        self.on_exception = on_exception
    def get_on_delivery(self):
        return self.on_delivery
    def set_on_delivery(self, on_delivery):
        self.on_delivery = on_delivery
    def validate_EmailType(self, value):
        result = True
        # Validate type EmailType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EmailType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_EmailType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_EmailType_patterns_, ))
                result = False
        return result
    validate_EmailType_patterns_ = [["^((['_A-Za-z0-9\\-\\+]+)(\\.['_A-Za-z0-9\\-\\+]+)*@([A-Za-z0-9-]+)(\\.[A-Za-z0-9-]+)*(\\.[A-Za-z]{2,5}))$"]]
    def _hasContent(self):
        if (
            self.email is not None or
            self.on_shipment is not None or
            self.on_exception is not None or
            self.on_delivery is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NotificationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NotificationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NotificationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NotificationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NotificationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NotificationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NotificationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.email is not None:
            namespaceprefix_ = self.email_nsprefix_ + ':' if (UseCapturedNS_ and self.email_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%semail>%s</%semail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.email), input_name='email')), namespaceprefix_ , eol_))
        if self.on_shipment is not None:
            namespaceprefix_ = self.on_shipment_nsprefix_ + ':' if (UseCapturedNS_ and self.on_shipment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%son-shipment>%s</%son-shipment>%s' % (namespaceprefix_ , self.gds_format_boolean(self.on_shipment, input_name='on-shipment'), namespaceprefix_ , eol_))
        if self.on_exception is not None:
            namespaceprefix_ = self.on_exception_nsprefix_ + ':' if (UseCapturedNS_ and self.on_exception_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%son-exception>%s</%son-exception>%s' % (namespaceprefix_ , self.gds_format_boolean(self.on_exception, input_name='on-exception'), namespaceprefix_ , eol_))
        if self.on_delivery is not None:
            namespaceprefix_ = self.on_delivery_nsprefix_ + ':' if (UseCapturedNS_ and self.on_delivery_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%son-delivery>%s</%son-delivery>%s' % (namespaceprefix_ , self.gds_format_boolean(self.on_delivery, input_name='on-delivery'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'email':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'email')
            value_ = self.gds_validate_string(value_, node, 'email')
            self.email = value_
            self.email_nsprefix_ = child_.prefix
            # validate type EmailType
            self.validate_EmailType(self.email)
        elif nodeName_ == 'on-shipment':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'on_shipment')
            ival_ = self.gds_validate_boolean(ival_, node, 'on_shipment')
            self.on_shipment = ival_
            self.on_shipment_nsprefix_ = child_.prefix
        elif nodeName_ == 'on-exception':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'on_exception')
            ival_ = self.gds_validate_boolean(ival_, node, 'on_exception')
            self.on_exception = ival_
            self.on_exception_nsprefix_ = child_.prefix
        elif nodeName_ == 'on-delivery':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'on_delivery')
            ival_ = self.gds_validate_boolean(ival_, node, 'on_delivery')
            self.on_delivery = ival_
            self.on_delivery_nsprefix_ = child_.prefix
# end class NotificationType


class PreferencesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, show_packing_instructions=None, show_postage_rate=None, show_insured_value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.show_packing_instructions = show_packing_instructions
        self.show_packing_instructions_nsprefix_ = None
        self.show_postage_rate = show_postage_rate
        self.show_postage_rate_nsprefix_ = None
        self.show_insured_value = show_insured_value
        self.show_insured_value_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PreferencesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PreferencesType.subclass:
            return PreferencesType.subclass(*args_, **kwargs_)
        else:
            return PreferencesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_show_packing_instructions(self):
        return self.show_packing_instructions
    def set_show_packing_instructions(self, show_packing_instructions):
        self.show_packing_instructions = show_packing_instructions
    def get_show_postage_rate(self):
        return self.show_postage_rate
    def set_show_postage_rate(self, show_postage_rate):
        self.show_postage_rate = show_postage_rate
    def get_show_insured_value(self):
        return self.show_insured_value
    def set_show_insured_value(self, show_insured_value):
        self.show_insured_value = show_insured_value
    def _hasContent(self):
        if (
            self.show_packing_instructions is not None or
            self.show_postage_rate is not None or
            self.show_insured_value is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PreferencesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PreferencesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PreferencesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PreferencesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PreferencesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PreferencesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PreferencesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.show_packing_instructions is not None:
            namespaceprefix_ = self.show_packing_instructions_nsprefix_ + ':' if (UseCapturedNS_ and self.show_packing_instructions_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshow-packing-instructions>%s</%sshow-packing-instructions>%s' % (namespaceprefix_ , self.gds_format_boolean(self.show_packing_instructions, input_name='show-packing-instructions'), namespaceprefix_ , eol_))
        if self.show_postage_rate is not None:
            namespaceprefix_ = self.show_postage_rate_nsprefix_ + ':' if (UseCapturedNS_ and self.show_postage_rate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshow-postage-rate>%s</%sshow-postage-rate>%s' % (namespaceprefix_ , self.gds_format_boolean(self.show_postage_rate, input_name='show-postage-rate'), namespaceprefix_ , eol_))
        if self.show_insured_value is not None:
            namespaceprefix_ = self.show_insured_value_nsprefix_ + ':' if (UseCapturedNS_ and self.show_insured_value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshow-insured-value>%s</%sshow-insured-value>%s' % (namespaceprefix_ , self.gds_format_boolean(self.show_insured_value, input_name='show-insured-value'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'show-packing-instructions':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'show_packing_instructions')
            ival_ = self.gds_validate_boolean(ival_, node, 'show_packing_instructions')
            self.show_packing_instructions = ival_
            self.show_packing_instructions_nsprefix_ = child_.prefix
        elif nodeName_ == 'show-postage-rate':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'show_postage_rate')
            ival_ = self.gds_validate_boolean(ival_, node, 'show_postage_rate')
            self.show_postage_rate = ival_
            self.show_postage_rate_nsprefix_ = child_.prefix
        elif nodeName_ == 'show-insured-value':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'show_insured_value')
            ival_ = self.gds_validate_boolean(ival_, node, 'show_insured_value')
            self.show_insured_value = ival_
            self.show_insured_value_nsprefix_ = child_.prefix
# end class PreferencesType


class ReferencesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, cost_centre=None, customer_ref_1=None, customer_ref_2=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.cost_centre = cost_centre
        self.validate_CostCentreIDType(self.cost_centre)
        self.cost_centre_nsprefix_ = None
        self.customer_ref_1 = customer_ref_1
        self.validate_customer_ref_1Type(self.customer_ref_1)
        self.customer_ref_1_nsprefix_ = None
        self.customer_ref_2 = customer_ref_2
        self.validate_customer_ref_2Type(self.customer_ref_2)
        self.customer_ref_2_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReferencesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReferencesType.subclass:
            return ReferencesType.subclass(*args_, **kwargs_)
        else:
            return ReferencesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_cost_centre(self):
        return self.cost_centre
    def set_cost_centre(self, cost_centre):
        self.cost_centre = cost_centre
    def get_customer_ref_1(self):
        return self.customer_ref_1
    def set_customer_ref_1(self, customer_ref_1):
        self.customer_ref_1 = customer_ref_1
    def get_customer_ref_2(self):
        return self.customer_ref_2
    def set_customer_ref_2(self, customer_ref_2):
        self.customer_ref_2 = customer_ref_2
    def validate_CostCentreIDType(self, value):
        result = True
        # Validate type CostCentreIDType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CostCentreIDType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_customer_ref_1Type(self, value):
        result = True
        # Validate type customer-ref-1Type, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 35:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on customer-ref-1Type' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_customer_ref_2Type(self, value):
        result = True
        # Validate type customer-ref-2Type, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 35:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on customer-ref-2Type' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.cost_centre is not None or
            self.customer_ref_1 is not None or
            self.customer_ref_2 is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ReferencesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReferencesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReferencesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReferencesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReferencesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ReferencesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ReferencesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cost_centre is not None:
            namespaceprefix_ = self.cost_centre_nsprefix_ + ':' if (UseCapturedNS_ and self.cost_centre_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scost-centre>%s</%scost-centre>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cost_centre), input_name='cost-centre')), namespaceprefix_ , eol_))
        if self.customer_ref_1 is not None:
            namespaceprefix_ = self.customer_ref_1_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_ref_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-ref-1>%s</%scustomer-ref-1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_ref_1), input_name='customer-ref-1')), namespaceprefix_ , eol_))
        if self.customer_ref_2 is not None:
            namespaceprefix_ = self.customer_ref_2_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_ref_2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-ref-2>%s</%scustomer-ref-2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_ref_2), input_name='customer-ref-2')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'cost-centre':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cost_centre')
            value_ = self.gds_validate_string(value_, node, 'cost_centre')
            self.cost_centre = value_
            self.cost_centre_nsprefix_ = child_.prefix
            # validate type CostCentreIDType
            self.validate_CostCentreIDType(self.cost_centre)
        elif nodeName_ == 'customer-ref-1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customer_ref_1')
            value_ = self.gds_validate_string(value_, node, 'customer_ref_1')
            self.customer_ref_1 = value_
            self.customer_ref_1_nsprefix_ = child_.prefix
            # validate type customer-ref-1Type
            self.validate_customer_ref_1Type(self.customer_ref_1)
        elif nodeName_ == 'customer-ref-2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customer_ref_2')
            value_ = self.gds_validate_string(value_, node, 'customer_ref_2')
            self.customer_ref_2 = value_
            self.customer_ref_2_nsprefix_ = child_.prefix
            # validate type customer-ref-2Type
            self.validate_customer_ref_2Type(self.customer_ref_2)
# end class ReferencesType


class SettlementInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, promo_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.promo_code = promo_code
        self.validate_PromoCodeType(self.promo_code)
        self.promo_code_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SettlementInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SettlementInfoType.subclass:
            return SettlementInfoType.subclass(*args_, **kwargs_)
        else:
            return SettlementInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_promo_code(self):
        return self.promo_code
    def set_promo_code(self, promo_code):
        self.promo_code = promo_code
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
        return result
    def _hasContent(self):
        if (
            self.promo_code is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SettlementInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SettlementInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SettlementInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SettlementInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SettlementInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SettlementInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SettlementInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.promo_code is not None:
            namespaceprefix_ = self.promo_code_nsprefix_ + ':' if (UseCapturedNS_ and self.promo_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spromo-code>%s</%spromo-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.promo_code), input_name='promo-code')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'promo-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'promo_code')
            value_ = self.gds_validate_string(value_, node, 'promo_code')
            self.promo_code = value_
            self.promo_code_nsprefix_ = child_.prefix
            # validate type PromoCodeType
            self.validate_PromoCodeType(self.promo_code)
# end class SettlementInfoType


class NonContractShipmentRefundRequestType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, email=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.email = email
        self.validate_EmailType(self.email)
        self.email_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonContractShipmentRefundRequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonContractShipmentRefundRequestType.subclass:
            return NonContractShipmentRefundRequestType.subclass(*args_, **kwargs_)
        else:
            return NonContractShipmentRefundRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def validate_EmailType(self, value):
        result = True
        # Validate type EmailType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EmailType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_EmailType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_EmailType_patterns_, ))
                result = False
        return result
    validate_EmailType_patterns_ = [["^((['_A-Za-z0-9\\-\\+]+)(\\.['_A-Za-z0-9\\-\\+]+)*@([A-Za-z0-9-]+)(\\.[A-Za-z0-9-]+)*(\\.[A-Za-z]{2,5}))$"]]
    def _hasContent(self):
        if (
            self.email is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentRefundRequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonContractShipmentRefundRequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonContractShipmentRefundRequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonContractShipmentRefundRequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonContractShipmentRefundRequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonContractShipmentRefundRequestType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentRefundRequestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.email is not None:
            namespaceprefix_ = self.email_nsprefix_ + ':' if (UseCapturedNS_ and self.email_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%semail>%s</%semail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.email), input_name='email')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'email':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'email')
            value_ = self.gds_validate_string(value_, node, 'email')
            self.email = value_
            self.email_nsprefix_ = child_.prefix
            # validate type EmailType
            self.validate_EmailType(self.email)
# end class NonContractShipmentRefundRequestType


class NonContractShipmentRefundRequestInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service_ticket_date=None, service_ticket_id=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if isinstance(service_ticket_date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(service_ticket_date, '%Y-%m-%d').date()
        else:
            initvalue_ = service_ticket_date
        self.service_ticket_date = initvalue_
        self.service_ticket_date_nsprefix_ = None
        self.service_ticket_id = service_ticket_id
        self.service_ticket_id_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonContractShipmentRefundRequestInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonContractShipmentRefundRequestInfoType.subclass:
            return NonContractShipmentRefundRequestInfoType.subclass(*args_, **kwargs_)
        else:
            return NonContractShipmentRefundRequestInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_service_ticket_date(self):
        return self.service_ticket_date
    def set_service_ticket_date(self, service_ticket_date):
        self.service_ticket_date = service_ticket_date
    def get_service_ticket_id(self):
        return self.service_ticket_id
    def set_service_ticket_id(self, service_ticket_id):
        self.service_ticket_id = service_ticket_id
    def _hasContent(self):
        if (
            self.service_ticket_date is not None or
            self.service_ticket_id is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentRefundRequestInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonContractShipmentRefundRequestInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonContractShipmentRefundRequestInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonContractShipmentRefundRequestInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonContractShipmentRefundRequestInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonContractShipmentRefundRequestInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NonContractShipmentRefundRequestInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.service_ticket_date is not None:
            namespaceprefix_ = self.service_ticket_date_nsprefix_ + ':' if (UseCapturedNS_ and self.service_ticket_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-ticket-date>%s</%sservice-ticket-date>%s' % (namespaceprefix_ , self.gds_format_date(self.service_ticket_date, input_name='service-ticket-date'), namespaceprefix_ , eol_))
        if self.service_ticket_id is not None:
            namespaceprefix_ = self.service_ticket_id_nsprefix_ + ':' if (UseCapturedNS_ and self.service_ticket_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-ticket-id>%s</%sservice-ticket-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_ticket_id), input_name='service-ticket-id')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'service-ticket-date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.service_ticket_date = dval_
            self.service_ticket_date_nsprefix_ = child_.prefix
        elif nodeName_ == 'service-ticket-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'service_ticket_id')
            value_ = self.gds_validate_string(value_, node, 'service_ticket_id')
            self.service_ticket_id = value_
            self.service_ticket_id_nsprefix_ = child_.prefix
# end class NonContractShipmentRefundRequestInfoType


class delivery_specType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service_code=None, sender=None, destination=None, recipient=None, options=None, parcel_characteristics=None, notification=None, preferences=None, references=None, customs=None, settlement_info=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.service_code = service_code
        self.service_code_nsprefix_ = None
        self.sender = sender
        self.sender_nsprefix_ = None
        self.destination = destination
        self.destination_nsprefix_ = None
        self.recipient = recipient
        self.recipient_nsprefix_ = None
        self.options = options
        self.options_nsprefix_ = None
        self.parcel_characteristics = parcel_characteristics
        self.parcel_characteristics_nsprefix_ = None
        self.notification = notification
        self.notification_nsprefix_ = None
        self.preferences = preferences
        self.preferences_nsprefix_ = None
        self.references = references
        self.references_nsprefix_ = None
        self.customs = customs
        self.customs_nsprefix_ = None
        self.settlement_info = settlement_info
        self.settlement_info_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, delivery_specType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if delivery_specType.subclass:
            return delivery_specType.subclass(*args_, **kwargs_)
        else:
            return delivery_specType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_service_code(self):
        return self.service_code
    def set_service_code(self, service_code):
        self.service_code = service_code
    def get_sender(self):
        return self.sender
    def set_sender(self, sender):
        self.sender = sender
    def get_destination(self):
        return self.destination
    def set_destination(self, destination):
        self.destination = destination
    def get_recipient(self):
        return self.recipient
    def set_recipient(self, recipient):
        self.recipient = recipient
    def get_options(self):
        return self.options
    def set_options(self, options):
        self.options = options
    def get_parcel_characteristics(self):
        return self.parcel_characteristics
    def set_parcel_characteristics(self, parcel_characteristics):
        self.parcel_characteristics = parcel_characteristics
    def get_notification(self):
        return self.notification
    def set_notification(self, notification):
        self.notification = notification
    def get_preferences(self):
        return self.preferences
    def set_preferences(self, preferences):
        self.preferences = preferences
    def get_references(self):
        return self.references
    def set_references(self, references):
        self.references = references
    def get_customs(self):
        return self.customs
    def set_customs(self, customs):
        self.customs = customs
    def get_settlement_info(self):
        return self.settlement_info
    def set_settlement_info(self, settlement_info):
        self.settlement_info = settlement_info
    def _hasContent(self):
        if (
            self.service_code is not None or
            self.sender is not None or
            self.destination is not None or
            self.recipient is not None or
            self.options is not None or
            self.parcel_characteristics is not None or
            self.notification is not None or
            self.preferences is not None or
            self.references is not None or
            self.customs is not None or
            self.settlement_info is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='delivery-specType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('delivery-specType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'delivery-specType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='delivery-specType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='delivery-specType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='delivery-specType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='delivery-specType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.service_code is not None:
            namespaceprefix_ = self.service_code_nsprefix_ + ':' if (UseCapturedNS_ and self.service_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-code>%s</%sservice-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_code), input_name='service-code')), namespaceprefix_ , eol_))
        if self.sender is not None:
            namespaceprefix_ = self.sender_nsprefix_ + ':' if (UseCapturedNS_ and self.sender_nsprefix_) else ''
            self.sender.export(outfile, level, namespaceprefix_, namespacedef_='', name_='sender', pretty_print=pretty_print)
        if self.destination is not None:
            namespaceprefix_ = self.destination_nsprefix_ + ':' if (UseCapturedNS_ and self.destination_nsprefix_) else ''
            self.destination.export(outfile, level, namespaceprefix_, namespacedef_='', name_='destination', pretty_print=pretty_print)
        if self.recipient is not None:
            namespaceprefix_ = self.recipient_nsprefix_ + ':' if (UseCapturedNS_ and self.recipient_nsprefix_) else ''
            self.recipient.export(outfile, level, namespaceprefix_, namespacedef_='', name_='recipient', pretty_print=pretty_print)
        if self.options is not None:
            namespaceprefix_ = self.options_nsprefix_ + ':' if (UseCapturedNS_ and self.options_nsprefix_) else ''
            self.options.export(outfile, level, namespaceprefix_, namespacedef_='', name_='options', pretty_print=pretty_print)
        if self.parcel_characteristics is not None:
            namespaceprefix_ = self.parcel_characteristics_nsprefix_ + ':' if (UseCapturedNS_ and self.parcel_characteristics_nsprefix_) else ''
            self.parcel_characteristics.export(outfile, level, namespaceprefix_, namespacedef_='', name_='parcel-characteristics', pretty_print=pretty_print)
        if self.notification is not None:
            namespaceprefix_ = self.notification_nsprefix_ + ':' if (UseCapturedNS_ and self.notification_nsprefix_) else ''
            self.notification.export(outfile, level, namespaceprefix_, namespacedef_='', name_='notification', pretty_print=pretty_print)
        if self.preferences is not None:
            namespaceprefix_ = self.preferences_nsprefix_ + ':' if (UseCapturedNS_ and self.preferences_nsprefix_) else ''
            self.preferences.export(outfile, level, namespaceprefix_, namespacedef_='', name_='preferences', pretty_print=pretty_print)
        if self.references is not None:
            namespaceprefix_ = self.references_nsprefix_ + ':' if (UseCapturedNS_ and self.references_nsprefix_) else ''
            self.references.export(outfile, level, namespaceprefix_, namespacedef_='', name_='references', pretty_print=pretty_print)
        if self.customs is not None:
            namespaceprefix_ = self.customs_nsprefix_ + ':' if (UseCapturedNS_ and self.customs_nsprefix_) else ''
            self.customs.export(outfile, level, namespaceprefix_, namespacedef_='', name_='customs', pretty_print=pretty_print)
        if self.settlement_info is not None:
            namespaceprefix_ = self.settlement_info_nsprefix_ + ':' if (UseCapturedNS_ and self.settlement_info_nsprefix_) else ''
            self.settlement_info.export(outfile, level, namespaceprefix_, namespacedef_='', name_='settlement-info', pretty_print=pretty_print)
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
        elif nodeName_ == 'sender':
            obj_ = SenderType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.sender = obj_
            obj_.original_tagname_ = 'sender'
        elif nodeName_ == 'destination':
            obj_ = DestinationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.destination = obj_
            obj_.original_tagname_ = 'destination'
        elif nodeName_ == 'recipient':
            obj_ = RecipientAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.recipient = obj_
            obj_.original_tagname_ = 'recipient'
        elif nodeName_ == 'options':
            obj_ = optionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.options = obj_
            obj_.original_tagname_ = 'options'
        elif nodeName_ == 'parcel-characteristics':
            obj_ = ParcelCharacteristicsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.parcel_characteristics = obj_
            obj_.original_tagname_ = 'parcel-characteristics'
        elif nodeName_ == 'notification':
            obj_ = NotificationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.notification = obj_
            obj_.original_tagname_ = 'notification'
        elif nodeName_ == 'preferences':
            obj_ = PreferencesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.preferences = obj_
            obj_.original_tagname_ = 'preferences'
        elif nodeName_ == 'references':
            obj_ = ReferencesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.references = obj_
            obj_.original_tagname_ = 'references'
        elif nodeName_ == 'customs':
            obj_ = CustomsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customs = obj_
            obj_.original_tagname_ = 'customs'
        elif nodeName_ == 'settlement-info':
            obj_ = SettlementInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.settlement_info = obj_
            obj_.original_tagname_ = 'settlement-info'
# end class delivery_specType


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
            obj_ = OptionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.option.append(obj_)
            obj_.original_tagname_ = 'option'
# end class optionsType


class priced_optionsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, priced_option=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if priced_option is None:
            self.priced_option = []
        else:
            self.priced_option = priced_option
        self.priced_option_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, priced_optionsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if priced_optionsType.subclass:
            return priced_optionsType.subclass(*args_, **kwargs_)
        else:
            return priced_optionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_priced_option(self):
        return self.priced_option
    def set_priced_option(self, priced_option):
        self.priced_option = priced_option
    def add_priced_option(self, value):
        self.priced_option.append(value)
    def insert_priced_option_at(self, index, value):
        self.priced_option.insert(index, value)
    def replace_priced_option_at(self, index, value):
        self.priced_option[index] = value
    def _hasContent(self):
        if (
            self.priced_option
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='priced-optionsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('priced-optionsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'priced-optionsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='priced-optionsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='priced-optionsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='priced-optionsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='priced-optionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for priced_option_ in self.priced_option:
            namespaceprefix_ = self.priced_option_nsprefix_ + ':' if (UseCapturedNS_ and self.priced_option_nsprefix_) else ''
            priced_option_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='priced-option', pretty_print=pretty_print)
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
        if nodeName_ == 'priced-option':
            obj_ = priced_optionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.priced_option.append(obj_)
            obj_.original_tagname_ = 'priced-option'
# end class priced_optionsType


class priced_optionType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, option_code=None, option_price=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.option_code = option_code
        self.validate_option_codeType(self.option_code)
        self.option_code_nsprefix_ = None
        self.option_price = option_price
        self.option_price_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, priced_optionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if priced_optionType.subclass:
            return priced_optionType.subclass(*args_, **kwargs_)
        else:
            return priced_optionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_option_code(self):
        return self.option_code
    def set_option_code(self, option_code):
        self.option_code = option_code
    def get_option_price(self):
        return self.option_price
    def set_option_price(self, option_price):
        self.option_price = option_price
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
        return result
    def _hasContent(self):
        if (
            self.option_code is not None or
            self.option_price is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='priced-optionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('priced-optionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'priced-optionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='priced-optionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='priced-optionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='priced-optionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='priced-optionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.option_code is not None:
            namespaceprefix_ = self.option_code_nsprefix_ + ':' if (UseCapturedNS_ and self.option_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-code>%s</%soption-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.option_code), input_name='option-code')), namespaceprefix_ , eol_))
        if self.option_price is not None:
            namespaceprefix_ = self.option_price_nsprefix_ + ':' if (UseCapturedNS_ and self.option_price_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soption-price>%s</%soption-price>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.option_price), input_name='option-price')), namespaceprefix_ , eol_))
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
        elif nodeName_ == 'option-price':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'option_price')
            value_ = self.gds_validate_string(value_, node, 'option_price')
            self.option_price = value_
            self.option_price_nsprefix_ = child_.prefix
# end class priced_optionType


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
    def __init__(self, adjustment_code=None, adjustment_amount=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.adjustment_code = adjustment_code
        self.validate_adjustment_codeType(self.adjustment_code)
        self.adjustment_code_nsprefix_ = None
        self.adjustment_amount = adjustment_amount
        self.adjustment_amount_nsprefix_ = None
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
    def get_adjustment_amount(self):
        return self.adjustment_amount
    def set_adjustment_amount(self, adjustment_amount):
        self.adjustment_amount = adjustment_amount
    def validate_adjustment_codeType(self, value):
        result = True
        # Validate type adjustment-codeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on adjustment-codeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.adjustment_code is not None or
            self.adjustment_amount is not None
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
        if self.adjustment_amount is not None:
            namespaceprefix_ = self.adjustment_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.adjustment_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadjustment-amount>%s</%sadjustment-amount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.adjustment_amount), input_name='adjustment-amount')), namespaceprefix_ , eol_))
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
            # validate type adjustment-codeType
            self.validate_adjustment_codeType(self.adjustment_code)
        elif nodeName_ == 'adjustment-amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'adjustment_amount')
            value_ = self.gds_validate_string(value_, node, 'adjustment_amount')
            self.adjustment_amount = value_
            self.adjustment_amount_nsprefix_ = child_.prefix
# end class adjustmentType


class cc_receipt_detailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, merchant_name=None, merchant_url=None, name_on_card=None, auth_code=None, auth_timestamp=None, card_type=None, charge_amount=None, currency=None, transaction_type=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.merchant_name = merchant_name
        self.validate_merchant_nameType(self.merchant_name)
        self.merchant_name_nsprefix_ = None
        self.merchant_url = merchant_url
        self.validate_merchant_urlType(self.merchant_url)
        self.merchant_url_nsprefix_ = None
        self.name_on_card = name_on_card
        self.name_on_card_nsprefix_ = None
        self.auth_code = auth_code
        self.auth_code_nsprefix_ = None
        if isinstance(auth_timestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(auth_timestamp, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = auth_timestamp
        self.auth_timestamp = initvalue_
        self.auth_timestamp_nsprefix_ = None
        self.card_type = card_type
        self.card_type_nsprefix_ = None
        self.charge_amount = charge_amount
        self.charge_amount_nsprefix_ = None
        self.currency = currency
        self.currency_nsprefix_ = None
        self.transaction_type = transaction_type
        self.validate_transaction_typeType(self.transaction_type)
        self.transaction_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, cc_receipt_detailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if cc_receipt_detailsType.subclass:
            return cc_receipt_detailsType.subclass(*args_, **kwargs_)
        else:
            return cc_receipt_detailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_merchant_name(self):
        return self.merchant_name
    def set_merchant_name(self, merchant_name):
        self.merchant_name = merchant_name
    def get_merchant_url(self):
        return self.merchant_url
    def set_merchant_url(self, merchant_url):
        self.merchant_url = merchant_url
    def get_name_on_card(self):
        return self.name_on_card
    def set_name_on_card(self, name_on_card):
        self.name_on_card = name_on_card
    def get_auth_code(self):
        return self.auth_code
    def set_auth_code(self, auth_code):
        self.auth_code = auth_code
    def get_auth_timestamp(self):
        return self.auth_timestamp
    def set_auth_timestamp(self, auth_timestamp):
        self.auth_timestamp = auth_timestamp
    def get_card_type(self):
        return self.card_type
    def set_card_type(self, card_type):
        self.card_type = card_type
    def get_charge_amount(self):
        return self.charge_amount
    def set_charge_amount(self, charge_amount):
        self.charge_amount = charge_amount
    def get_currency(self):
        return self.currency
    def set_currency(self, currency):
        self.currency = currency
    def get_transaction_type(self):
        return self.transaction_type
    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type
    def validate_merchant_nameType(self, value):
        result = True
        # Validate type merchant-nameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchant-nameType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_merchant_urlType(self, value):
        result = True
        # Validate type merchant-urlType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchant-urlType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_transaction_typeType(self, value):
        result = True
        # Validate type transaction-typeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on transaction-typeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.merchant_name is not None or
            self.merchant_url is not None or
            self.name_on_card is not None or
            self.auth_code is not None or
            self.auth_timestamp is not None or
            self.card_type is not None or
            self.charge_amount is not None or
            self.currency is not None or
            self.transaction_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='cc-receipt-detailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('cc-receipt-detailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'cc-receipt-detailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='cc-receipt-detailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='cc-receipt-detailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='cc-receipt-detailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='cc-receipt-detailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.merchant_name is not None:
            namespaceprefix_ = self.merchant_name_nsprefix_ + ':' if (UseCapturedNS_ and self.merchant_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smerchant-name>%s</%smerchant-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.merchant_name), input_name='merchant-name')), namespaceprefix_ , eol_))
        if self.merchant_url is not None:
            namespaceprefix_ = self.merchant_url_nsprefix_ + ':' if (UseCapturedNS_ and self.merchant_url_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smerchant-url>%s</%smerchant-url>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.merchant_url), input_name='merchant-url')), namespaceprefix_ , eol_))
        if self.name_on_card is not None:
            namespaceprefix_ = self.name_on_card_nsprefix_ + ':' if (UseCapturedNS_ and self.name_on_card_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname-on-card>%s</%sname-on-card>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.name_on_card), input_name='name-on-card')), namespaceprefix_ , eol_))
        if self.auth_code is not None:
            namespaceprefix_ = self.auth_code_nsprefix_ + ':' if (UseCapturedNS_ and self.auth_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauth-code>%s</%sauth-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.auth_code), input_name='auth-code')), namespaceprefix_ , eol_))
        if self.auth_timestamp is not None:
            namespaceprefix_ = self.auth_timestamp_nsprefix_ + ':' if (UseCapturedNS_ and self.auth_timestamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauth-timestamp>%s</%sauth-timestamp>%s' % (namespaceprefix_ , self.gds_format_datetime(self.auth_timestamp, input_name='auth-timestamp'), namespaceprefix_ , eol_))
        if self.card_type is not None:
            namespaceprefix_ = self.card_type_nsprefix_ + ':' if (UseCapturedNS_ and self.card_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scard-type>%s</%scard-type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.card_type), input_name='card-type')), namespaceprefix_ , eol_))
        if self.charge_amount is not None:
            namespaceprefix_ = self.charge_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.charge_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scharge-amount>%s</%scharge-amount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.charge_amount), input_name='charge-amount')), namespaceprefix_ , eol_))
        if self.currency is not None:
            namespaceprefix_ = self.currency_nsprefix_ + ':' if (UseCapturedNS_ and self.currency_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scurrency>%s</%scurrency>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.currency), input_name='currency')), namespaceprefix_ , eol_))
        if self.transaction_type is not None:
            namespaceprefix_ = self.transaction_type_nsprefix_ + ':' if (UseCapturedNS_ and self.transaction_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransaction-type>%s</%stransaction-type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.transaction_type), input_name='transaction-type')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'merchant-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchant_name')
            value_ = self.gds_validate_string(value_, node, 'merchant_name')
            self.merchant_name = value_
            self.merchant_name_nsprefix_ = child_.prefix
            # validate type merchant-nameType
            self.validate_merchant_nameType(self.merchant_name)
        elif nodeName_ == 'merchant-url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchant_url')
            value_ = self.gds_validate_string(value_, node, 'merchant_url')
            self.merchant_url = value_
            self.merchant_url_nsprefix_ = child_.prefix
            # validate type merchant-urlType
            self.validate_merchant_urlType(self.merchant_url)
        elif nodeName_ == 'name-on-card':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name_on_card')
            value_ = self.gds_validate_string(value_, node, 'name_on_card')
            self.name_on_card = value_
            self.name_on_card_nsprefix_ = child_.prefix
        elif nodeName_ == 'auth-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'auth_code')
            value_ = self.gds_validate_string(value_, node, 'auth_code')
            self.auth_code = value_
            self.auth_code_nsprefix_ = child_.prefix
        elif nodeName_ == 'auth-timestamp':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.auth_timestamp = dval_
            self.auth_timestamp_nsprefix_ = child_.prefix
        elif nodeName_ == 'card-type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'card_type')
            value_ = self.gds_validate_string(value_, node, 'card_type')
            self.card_type = value_
            self.card_type_nsprefix_ = child_.prefix
        elif nodeName_ == 'charge-amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'charge_amount')
            value_ = self.gds_validate_string(value_, node, 'charge_amount')
            self.charge_amount = value_
            self.charge_amount_nsprefix_ = child_.prefix
        elif nodeName_ == 'currency':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'currency')
            value_ = self.gds_validate_string(value_, node, 'currency')
            self.currency = value_
            self.currency_nsprefix_ = child_.prefix
        elif nodeName_ == 'transaction-type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'transaction_type')
            value_ = self.gds_validate_string(value_, node, 'transaction_type')
            self.transaction_type = value_
            self.transaction_type_nsprefix_ = child_.prefix
            # validate type transaction-typeType
            self.validate_transaction_typeType(self.transaction_type)
# end class cc_receipt_detailsType


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
            obj_ = OptionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.option.append(obj_)
            obj_.original_tagname_ = 'option'
# end class optionsType1


class sku_listType(GeneratedsSuper):
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
                CurrentSubclassModule_, sku_listType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if sku_listType.subclass:
            return sku_listType.subclass(*args_, **kwargs_)
        else:
            return sku_listType(*args_, **kwargs_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='sku-listType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('sku-listType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'sku-listType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='sku-listType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='sku-listType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='sku-listType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='sku-listType', fromsubclass_=False, pretty_print=True):
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
            obj_ = SkuType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class sku_listType


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
        rootTag = 'NonContractShipmentType'
        rootClass = NonContractShipmentType
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
        rootTag = 'NonContractShipmentType'
        rootClass = NonContractShipmentType
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
        rootTag = 'NonContractShipmentType'
        rootClass = NonContractShipmentType
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
        rootTag = 'NonContractShipmentType'
        rootClass = NonContractShipmentType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from ncshipment import *\n\n')
        sys.stdout.write('import ncshipment as model_\n\n')
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
NamespaceToDefMappings_ = {'http://www.canadapost.ca/ws/ncshipment-v4': [('CostCentreIDType',
                                                './schemas/ncshipment.xsd',
                                                'ST'),
                                               ('EmailType',
                                                './schemas/ncshipment.xsd',
                                                'ST'),
                                               ('CompanyNameType',
                                                './schemas/ncshipment.xsd',
                                                'ST'),
                                               ('ContactNameType',
                                                './schemas/ncshipment.xsd',
                                                'ST'),
                                               ('TrackingPINType',
                                                './schemas/ncshipment.xsd',
                                                'ST'),
                                               ('ShipmentIDType',
                                                './schemas/ncshipment.xsd',
                                                'ST'),
                                               ('PromoCodeType',
                                                './schemas/ncshipment.xsd',
                                                'ST'),
                                               ('NonContractShipmentInfoType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('NonContractShipmentDetailsType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('NonContractShipmentReceiptType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('NonContractShipmentType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('NonContractShipmentsType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('DeliverySpecType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('CustomsType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('SkuType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('SenderType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('RecipientAddressType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('DestinationType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('DomesticAddressDetailsType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('AddressDetailsType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('DestinationAddressDetailsType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('OptionType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('ParcelCharacteristicsType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('NotificationType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('PreferencesType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('ReferencesType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('SettlementInfoType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('NonContractShipmentRefundRequestType',
                                                './schemas/ncshipment.xsd',
                                                'CT'),
                                               ('NonContractShipmentRefundRequestInfoType',
                                                './schemas/ncshipment.xsd',
                                                'CT')]}

__all__ = [
    "AddressDetailsType",
    "CustomsType",
    "DeliverySpecType",
    "DestinationAddressDetailsType",
    "DestinationType",
    "DomesticAddressDetailsType",
    "NonContractShipmentDetailsType",
    "NonContractShipmentInfoType",
    "NonContractShipmentReceiptType",
    "NonContractShipmentRefundRequestInfoType",
    "NonContractShipmentRefundRequestType",
    "NonContractShipmentType",
    "NonContractShipmentsType",
    "NotificationType",
    "OptionType",
    "ParcelCharacteristicsType",
    "PreferencesType",
    "RecipientAddressType",
    "ReferencesType",
    "SenderType",
    "SettlementInfoType",
    "SkuType",
    "adjustmentType",
    "adjustmentsType",
    "cc_receipt_detailsType",
    "delivery_specType",
    "dimensionsType",
    "optionsType",
    "optionsType1",
    "priced_optionType",
    "priced_optionsType",
    "service_standardType",
    "sku_listType"
]
