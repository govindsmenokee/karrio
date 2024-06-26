#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Jul 14 15:39:45 2021 by generateDS.py version 2.39.2.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './canadapost_lib/postoffice.py')
#
# Command line arguments:
#   ./schemas/postoffice.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-carriers/.venv/karrio-carriers/bin/generateDS --no-namespace-defs -o "./canadapost_lib/postoffice.py" ./schemas/postoffice.xsd
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


class dayType(str, Enum):
    _1='1'
    _2='2'
    _3='3'
    _4='4'
    _5='5'
    _6='6'
    _7='7'


class post_office_list(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, post_office=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if post_office is None:
            self.post_office = []
        else:
            self.post_office = post_office
        self.post_office_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, post_office_list)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if post_office_list.subclass:
            return post_office_list.subclass(*args_, **kwargs_)
        else:
            return post_office_list(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_post_office(self):
        return self.post_office
    def set_post_office(self, post_office):
        self.post_office = post_office
    def add_post_office(self, value):
        self.post_office.append(value)
    def insert_post_office_at(self, index, value):
        self.post_office.insert(index, value)
    def replace_post_office_at(self, index, value):
        self.post_office[index] = value
    def _hasContent(self):
        if (
            self.post_office
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='post-office-list', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('post-office-list')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'post-office-list':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='post-office-list')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='post-office-list', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='post-office-list'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='post-office-list', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for post_office_ in self.post_office:
            namespaceprefix_ = self.post_office_nsprefix_ + ':' if (UseCapturedNS_ and self.post_office_nsprefix_) else ''
            post_office_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='post-office', pretty_print=pretty_print)
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
        if nodeName_ == 'post-office':
            obj_ = post_officeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.post_office.append(obj_)
            obj_.original_tagname_ = 'post-office'
# end class post_office_list


class PostOfficeAddressType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, city=None, latitude=None, longitude=None, postal_code=None, province=None, office_address=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.city = city
        self.validate_cityType(self.city)
        self.city_nsprefix_ = None
        self.latitude = latitude
        self.validate_latitudeType(self.latitude)
        self.latitude_nsprefix_ = None
        self.longitude = longitude
        self.validate_longitudeType(self.longitude)
        self.longitude_nsprefix_ = None
        self.postal_code = postal_code
        self.postal_code_nsprefix_ = None
        self.province = province
        self.province_nsprefix_ = None
        self.office_address = office_address
        self.validate_office_addressType(self.office_address)
        self.office_address_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PostOfficeAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PostOfficeAddressType.subclass:
            return PostOfficeAddressType.subclass(*args_, **kwargs_)
        else:
            return PostOfficeAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_latitude(self):
        return self.latitude
    def set_latitude(self, latitude):
        self.latitude = latitude
    def get_longitude(self):
        return self.longitude
    def set_longitude(self, longitude):
        self.longitude = longitude
    def get_postal_code(self):
        return self.postal_code
    def set_postal_code(self, postal_code):
        self.postal_code = postal_code
    def get_province(self):
        return self.province
    def set_province(self, province):
        self.province = province
    def get_office_address(self):
        return self.office_address
    def set_office_address(self, office_address):
        self.office_address = office_address
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
    def validate_latitudeType(self, value):
        result = True
        # Validate type latitudeType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on latitudeType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 90:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on latitudeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_longitudeType(self, value):
        result = True
        # Validate type longitudeType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < -150:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on longitudeType' % {"value": value, "lineno": lineno} )
                result = False
            if value > -50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on longitudeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_office_addressType(self, value):
        result = True
        # Validate type office-addressType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 64:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on office-addressType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on office-addressType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.city is not None or
            self.latitude is not None or
            self.longitude is not None or
            self.postal_code is not None or
            self.province is not None or
            self.office_address is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PostOfficeAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PostOfficeAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PostOfficeAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PostOfficeAddressType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PostOfficeAddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PostOfficeAddressType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PostOfficeAddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.city is not None:
            namespaceprefix_ = self.city_nsprefix_ + ':' if (UseCapturedNS_ and self.city_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scity>%s</%scity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.city), input_name='city')), namespaceprefix_ , eol_))
        if self.latitude is not None:
            namespaceprefix_ = self.latitude_nsprefix_ + ':' if (UseCapturedNS_ and self.latitude_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slatitude>%s</%slatitude>%s' % (namespaceprefix_ , self.gds_format_decimal(self.latitude, input_name='latitude'), namespaceprefix_ , eol_))
        if self.longitude is not None:
            namespaceprefix_ = self.longitude_nsprefix_ + ':' if (UseCapturedNS_ and self.longitude_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slongitude>%s</%slongitude>%s' % (namespaceprefix_ , self.gds_format_decimal(self.longitude, input_name='longitude'), namespaceprefix_ , eol_))
        if self.postal_code is not None:
            namespaceprefix_ = self.postal_code_nsprefix_ + ':' if (UseCapturedNS_ and self.postal_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostal-code>%s</%spostal-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.postal_code), input_name='postal-code')), namespaceprefix_ , eol_))
        if self.province is not None:
            namespaceprefix_ = self.province_nsprefix_ + ':' if (UseCapturedNS_ and self.province_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprovince>%s</%sprovince>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.province), input_name='province')), namespaceprefix_ , eol_))
        if self.office_address is not None:
            namespaceprefix_ = self.office_address_nsprefix_ + ':' if (UseCapturedNS_ and self.office_address_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soffice-address>%s</%soffice-address>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.office_address), input_name='office-address')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type cityType
            self.validate_cityType(self.city)
        elif nodeName_ == 'latitude' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'latitude')
            fval_ = self.gds_validate_decimal(fval_, node, 'latitude')
            self.latitude = fval_
            self.latitude_nsprefix_ = child_.prefix
            # validate type latitudeType
            self.validate_latitudeType(self.latitude)
        elif nodeName_ == 'longitude' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'longitude')
            fval_ = self.gds_validate_decimal(fval_, node, 'longitude')
            self.longitude = fval_
            self.longitude_nsprefix_ = child_.prefix
            # validate type longitudeType
            self.validate_longitudeType(self.longitude)
        elif nodeName_ == 'postal-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postal_code')
            value_ = self.gds_validate_string(value_, node, 'postal_code')
            self.postal_code = value_
            self.postal_code_nsprefix_ = child_.prefix
        elif nodeName_ == 'province':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'province')
            value_ = self.gds_validate_string(value_, node, 'province')
            self.province = value_
            self.province_nsprefix_ = child_.prefix
        elif nodeName_ == 'office-address':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'office_address')
            value_ = self.gds_validate_string(value_, node, 'office_address')
            self.office_address = value_
            self.office_address_nsprefix_ = child_.prefix
            # validate type office-addressType
            self.validate_office_addressType(self.office_address)
# end class PostOfficeAddressType


class post_office_detail(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, address=None, location=None, name=None, office_id=None, bilingual_designation=None, hours_list=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.address = address
        self.address_nsprefix_ = None
        self.location = location
        self.validate_LocationType(self.location)
        self.location_nsprefix_ = None
        self.name = name
        self.validate_NameType(self.name)
        self.name_nsprefix_ = None
        self.office_id = office_id
        self.validate_OfficeIdType(self.office_id)
        self.office_id_nsprefix_ = None
        self.bilingual_designation = bilingual_designation
        self.bilingual_designation_nsprefix_ = None
        if hours_list is None:
            self.hours_list = []
        else:
            self.hours_list = hours_list
        self.hours_list_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, post_office_detail)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if post_office_detail.subclass:
            return post_office_detail.subclass(*args_, **kwargs_)
        else:
            return post_office_detail(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_location(self):
        return self.location
    def set_location(self, location):
        self.location = location
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_office_id(self):
        return self.office_id
    def set_office_id(self, office_id):
        self.office_id = office_id
    def get_bilingual_designation(self):
        return self.bilingual_designation
    def set_bilingual_designation(self, bilingual_designation):
        self.bilingual_designation = bilingual_designation
    def get_hours_list(self):
        return self.hours_list
    def set_hours_list(self, hours_list):
        self.hours_list = hours_list
    def add_hours_list(self, value):
        self.hours_list.append(value)
    def insert_hours_list_at(self, index, value):
        self.hours_list.insert(index, value)
    def replace_hours_list_at(self, index, value):
        self.hours_list[index] = value
    def validate_LocationType(self, value):
        result = True
        # Validate type LocationType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LocationType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_NameType(self, value):
        result = True
        # Validate type NameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on NameType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_OfficeIdType(self, value):
        result = True
        # Validate type OfficeIdType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_OfficeIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_OfficeIdType_patterns_, ))
                result = False
        return result
    validate_OfficeIdType_patterns_ = [['^(\\d{10})$']]
    def _hasContent(self):
        if (
            self.address is not None or
            self.location is not None or
            self.name is not None or
            self.office_id is not None or
            self.bilingual_designation is not None or
            self.hours_list
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='post-office-detail', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('post-office-detail')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'post-office-detail':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='post-office-detail')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='post-office-detail', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='post-office-detail'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='post-office-detail', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.address is not None:
            namespaceprefix_ = self.address_nsprefix_ + ':' if (UseCapturedNS_ and self.address_nsprefix_) else ''
            self.address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='address', pretty_print=pretty_print)
        if self.location is not None:
            namespaceprefix_ = self.location_nsprefix_ + ':' if (UseCapturedNS_ and self.location_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slocation>%s</%slocation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.location), input_name='location')), namespaceprefix_ , eol_))
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.name), input_name='name')), namespaceprefix_ , eol_))
        if self.office_id is not None:
            namespaceprefix_ = self.office_id_nsprefix_ + ':' if (UseCapturedNS_ and self.office_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soffice-id>%s</%soffice-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.office_id), input_name='office-id')), namespaceprefix_ , eol_))
        if self.bilingual_designation is not None:
            namespaceprefix_ = self.bilingual_designation_nsprefix_ + ':' if (UseCapturedNS_ and self.bilingual_designation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbilingual-designation>%s</%sbilingual-designation>%s' % (namespaceprefix_ , self.gds_format_boolean(self.bilingual_designation, input_name='bilingual-designation'), namespaceprefix_ , eol_))
        for hours_list_ in self.hours_list:
            namespaceprefix_ = self.hours_list_nsprefix_ + ':' if (UseCapturedNS_ and self.hours_list_nsprefix_) else ''
            hours_list_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='hours-list', pretty_print=pretty_print)
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
        if nodeName_ == 'address':
            obj_ = PostOfficeAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address = obj_
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'location':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'location')
            value_ = self.gds_validate_string(value_, node, 'location')
            self.location = value_
            self.location_nsprefix_ = child_.prefix
            # validate type LocationType
            self.validate_LocationType(self.location)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type NameType
            self.validate_NameType(self.name)
        elif nodeName_ == 'office-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'office_id')
            value_ = self.gds_validate_string(value_, node, 'office_id')
            self.office_id = value_
            self.office_id_nsprefix_ = child_.prefix
            # validate type OfficeIdType
            self.validate_OfficeIdType(self.office_id)
        elif nodeName_ == 'bilingual-designation':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'bilingual_designation')
            ival_ = self.gds_validate_boolean(ival_, node, 'bilingual_designation')
            self.bilingual_designation = ival_
            self.bilingual_designation_nsprefix_ = child_.prefix
        elif nodeName_ == 'hours-list':
            obj_ = hours_listType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.hours_list.append(obj_)
            obj_.original_tagname_ = 'hours-list'
# end class post_office_detail


class post_officeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, address=None, distance=None, location=None, name=None, office_id=None, bilingual_designation=None, link=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.address = address
        self.address_nsprefix_ = None
        self.distance = distance
        self.validate_distanceType(self.distance)
        self.distance_nsprefix_ = None
        self.location = location
        self.validate_LocationType(self.location)
        self.location_nsprefix_ = None
        self.name = name
        self.validate_NameType(self.name)
        self.name_nsprefix_ = None
        self.office_id = office_id
        self.validate_OfficeIdType(self.office_id)
        self.office_id_nsprefix_ = None
        self.bilingual_designation = bilingual_designation
        self.bilingual_designation_nsprefix_ = None
        self.link = link
        self.link_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, post_officeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if post_officeType.subclass:
            return post_officeType.subclass(*args_, **kwargs_)
        else:
            return post_officeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_distance(self):
        return self.distance
    def set_distance(self, distance):
        self.distance = distance
    def get_location(self):
        return self.location
    def set_location(self, location):
        self.location = location
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_office_id(self):
        return self.office_id
    def set_office_id(self, office_id):
        self.office_id = office_id
    def get_bilingual_designation(self):
        return self.bilingual_designation
    def set_bilingual_designation(self, bilingual_designation):
        self.bilingual_designation = bilingual_designation
    def get_link(self):
        return self.link
    def set_link(self, link):
        self.link = link
    def validate_distanceType(self, value):
        result = True
        # Validate type distanceType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on distanceType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 99999.99:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on distanceType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_LocationType(self, value):
        result = True
        # Validate type LocationType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on LocationType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_NameType(self, value):
        result = True
        # Validate type NameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on NameType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_OfficeIdType(self, value):
        result = True
        # Validate type OfficeIdType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_OfficeIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_OfficeIdType_patterns_, ))
                result = False
        return result
    validate_OfficeIdType_patterns_ = [['^(\\d{10})$']]
    def _hasContent(self):
        if (
            self.address is not None or
            self.distance is not None or
            self.location is not None or
            self.name is not None or
            self.office_id is not None or
            self.bilingual_designation is not None or
            self.link is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='post-officeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('post-officeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'post-officeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='post-officeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='post-officeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='post-officeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='post-officeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.address is not None:
            namespaceprefix_ = self.address_nsprefix_ + ':' if (UseCapturedNS_ and self.address_nsprefix_) else ''
            self.address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='address', pretty_print=pretty_print)
        if self.distance is not None:
            namespaceprefix_ = self.distance_nsprefix_ + ':' if (UseCapturedNS_ and self.distance_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdistance>%s</%sdistance>%s' % (namespaceprefix_ , self.gds_format_decimal(self.distance, input_name='distance'), namespaceprefix_ , eol_))
        if self.location is not None:
            namespaceprefix_ = self.location_nsprefix_ + ':' if (UseCapturedNS_ and self.location_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slocation>%s</%slocation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.location), input_name='location')), namespaceprefix_ , eol_))
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.name), input_name='name')), namespaceprefix_ , eol_))
        if self.office_id is not None:
            namespaceprefix_ = self.office_id_nsprefix_ + ':' if (UseCapturedNS_ and self.office_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soffice-id>%s</%soffice-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.office_id), input_name='office-id')), namespaceprefix_ , eol_))
        if self.bilingual_designation is not None:
            namespaceprefix_ = self.bilingual_designation_nsprefix_ + ':' if (UseCapturedNS_ and self.bilingual_designation_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbilingual-designation>%s</%sbilingual-designation>%s' % (namespaceprefix_ , self.gds_format_boolean(self.bilingual_designation, input_name='bilingual-designation'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'address':
            obj_ = PostOfficeAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address = obj_
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'distance' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'distance')
            fval_ = self.gds_validate_decimal(fval_, node, 'distance')
            self.distance = fval_
            self.distance_nsprefix_ = child_.prefix
            # validate type distanceType
            self.validate_distanceType(self.distance)
        elif nodeName_ == 'location':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'location')
            value_ = self.gds_validate_string(value_, node, 'location')
            self.location = value_
            self.location_nsprefix_ = child_.prefix
            # validate type LocationType
            self.validate_LocationType(self.location)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type NameType
            self.validate_NameType(self.name)
        elif nodeName_ == 'office-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'office_id')
            value_ = self.gds_validate_string(value_, node, 'office_id')
            self.office_id = value_
            self.office_id_nsprefix_ = child_.prefix
            # validate type OfficeIdType
            self.validate_OfficeIdType(self.office_id)
        elif nodeName_ == 'bilingual-designation':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'bilingual_designation')
            ival_ = self.gds_validate_boolean(ival_, node, 'bilingual_designation')
            self.bilingual_designation = ival_
            self.bilingual_designation_nsprefix_ = child_.prefix
        elif nodeName_ == 'link':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'link')
            value_ = self.gds_validate_string(value_, node, 'link')
            self.link = value_
            self.link_nsprefix_ = child_.prefix
# end class post_officeType


class hours_listType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, day=None, time=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.day = day
        self.validate_dayType(self.day)
        self.day_nsprefix_ = None
        if time is None:
            self.time = []
        else:
            self.time = time
        self.time_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, hours_listType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if hours_listType.subclass:
            return hours_listType.subclass(*args_, **kwargs_)
        else:
            return hours_listType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_day(self):
        return self.day
    def set_day(self, day):
        self.day = day
    def get_time(self):
        return self.time
    def set_time(self, time):
        self.time = time
    def add_time(self, value):
        self.time.append(value)
    def insert_time_at(self, index, value):
        self.time.insert(index, value)
    def replace_time_at(self, index, value):
        self.time[index] = value
    def validate_dayType(self, value):
        result = True
        # Validate type dayType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2', '3', '4', '5', '6', '7']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on dayType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.day is not None or
            self.time
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='hours-listType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('hours-listType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'hours-listType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='hours-listType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='hours-listType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='hours-listType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='hours-listType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.day is not None:
            namespaceprefix_ = self.day_nsprefix_ + ':' if (UseCapturedNS_ and self.day_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sday>%s</%sday>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.day), input_name='day')), namespaceprefix_ , eol_))
        for time_ in self.time:
            namespaceprefix_ = self.time_nsprefix_ + ':' if (UseCapturedNS_ and self.time_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stime>%s</%stime>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(time_), input_name='time')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'day':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'day')
            value_ = self.gds_validate_string(value_, node, 'day')
            self.day = value_
            self.day_nsprefix_ = child_.prefix
            # validate type dayType
            self.validate_dayType(self.day)
        elif nodeName_ == 'time':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'time')
            value_ = self.gds_validate_string(value_, node, 'time')
            self.time.append(value_)
            self.time_nsprefix_ = child_.prefix
# end class hours_listType


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
        rootTag = 'post_office_list'
        rootClass = post_office_list
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
        rootTag = 'post_office_list'
        rootClass = post_office_list
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
        rootTag = 'post_office_list'
        rootClass = post_office_list
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
        rootTag = 'post_office_list'
        rootClass = post_office_list
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from postoffice import *\n\n')
        sys.stdout.write('import postoffice as model_\n\n')
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
NamespaceToDefMappings_ = {'http://www.canadapost.ca/ws/postoffice': [('LocationType',
                                             './schemas/postoffice.xsd',
                                             'ST'),
                                            ('NameType',
                                             './schemas/postoffice.xsd',
                                             'ST'),
                                            ('OfficeIdType',
                                             './schemas/postoffice.xsd',
                                             'ST'),
                                            ('PostOfficeAddressType',
                                             './schemas/postoffice.xsd',
                                             'CT')]}

__all__ = [
    "PostOfficeAddressType",
    "hours_listType",
    "post_officeType",
    "post_office_detail",
    "post_office_list"
]
