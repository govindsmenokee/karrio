#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Jul 14 15:39:44 2021 by generateDS.py version 2.39.2.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './canadapost_lib/manifest.py')
#
# Command line arguments:
#   ./schemas/manifest.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-carriers/.venv/karrio-carriers/bin/generateDS --no-namespace-defs -o "./canadapost_lib/manifest.py" ./schemas/manifest.xsd
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
    ARTIFACT='artifact'
    DETAILS='details'
    MANIFEST_SHIPMENTS='manifestShipments'
    MANIFEST='manifest'
    SHIPMENT='shipment'


class country_codeType(str, Enum):
    CA='CA'
    US='US'


class ShipmentTransmitSetType(GeneratedsSuper):
    """customer-request-id -- For future use
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, customer_request_id=None, group_ids=None, cpc_pickup_indicator=None, requested_shipping_point=None, shipping_point_id=None, detailed_manifests=None, method_of_payment=None, manifest_address=None, customer_reference=None, excluded_shipments=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customer_request_id = customer_request_id
        self.validate_CustomerRequestIdType(self.customer_request_id)
        self.customer_request_id_nsprefix_ = None
        self.group_ids = group_ids
        self.group_ids_nsprefix_ = None
        self.cpc_pickup_indicator = cpc_pickup_indicator
        self.cpc_pickup_indicator_nsprefix_ = None
        self.requested_shipping_point = requested_shipping_point
        self.requested_shipping_point_nsprefix_ = None
        self.shipping_point_id = shipping_point_id
        self.shipping_point_id_nsprefix_ = None
        self.detailed_manifests = detailed_manifests
        self.detailed_manifests_nsprefix_ = None
        self.method_of_payment = method_of_payment
        self.method_of_payment_nsprefix_ = None
        self.manifest_address = manifest_address
        self.manifest_address_nsprefix_ = None
        self.customer_reference = customer_reference
        self.validate_CustomerReferenceType(self.customer_reference)
        self.customer_reference_nsprefix_ = None
        self.excluded_shipments = excluded_shipments
        self.excluded_shipments_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentTransmitSetType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentTransmitSetType.subclass:
            return ShipmentTransmitSetType.subclass(*args_, **kwargs_)
        else:
            return ShipmentTransmitSetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_customer_request_id(self):
        return self.customer_request_id
    def set_customer_request_id(self, customer_request_id):
        self.customer_request_id = customer_request_id
    def get_group_ids(self):
        return self.group_ids
    def set_group_ids(self, group_ids):
        self.group_ids = group_ids
    def get_cpc_pickup_indicator(self):
        return self.cpc_pickup_indicator
    def set_cpc_pickup_indicator(self, cpc_pickup_indicator):
        self.cpc_pickup_indicator = cpc_pickup_indicator
    def get_requested_shipping_point(self):
        return self.requested_shipping_point
    def set_requested_shipping_point(self, requested_shipping_point):
        self.requested_shipping_point = requested_shipping_point
    def get_shipping_point_id(self):
        return self.shipping_point_id
    def set_shipping_point_id(self, shipping_point_id):
        self.shipping_point_id = shipping_point_id
    def get_detailed_manifests(self):
        return self.detailed_manifests
    def set_detailed_manifests(self, detailed_manifests):
        self.detailed_manifests = detailed_manifests
    def get_method_of_payment(self):
        return self.method_of_payment
    def set_method_of_payment(self, method_of_payment):
        self.method_of_payment = method_of_payment
    def get_manifest_address(self):
        return self.manifest_address
    def set_manifest_address(self, manifest_address):
        self.manifest_address = manifest_address
    def get_customer_reference(self):
        return self.customer_reference
    def set_customer_reference(self, customer_reference):
        self.customer_reference = customer_reference
    def get_excluded_shipments(self):
        return self.excluded_shipments
    def set_excluded_shipments(self, excluded_shipments):
        self.excluded_shipments = excluded_shipments
    def validate_CustomerRequestIdType(self, value):
        result = True
        # Validate type CustomerRequestIdType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 35:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CustomerRequestIdType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_CustomerReferenceType(self, value):
        result = True
        # Validate type CustomerReferenceType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CustomerReferenceType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.customer_request_id is not None or
            self.group_ids is not None or
            self.cpc_pickup_indicator is not None or
            self.requested_shipping_point is not None or
            self.shipping_point_id is not None or
            self.detailed_manifests is not None or
            self.method_of_payment is not None or
            self.manifest_address is not None or
            self.customer_reference is not None or
            self.excluded_shipments is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentTransmitSetType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentTransmitSetType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentTransmitSetType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentTransmitSetType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentTransmitSetType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentTransmitSetType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentTransmitSetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.customer_request_id is not None:
            namespaceprefix_ = self.customer_request_id_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_request_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-request-id>%s</%scustomer-request-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_request_id), input_name='customer-request-id')), namespaceprefix_ , eol_))
        if self.group_ids is not None:
            namespaceprefix_ = self.group_ids_nsprefix_ + ':' if (UseCapturedNS_ and self.group_ids_nsprefix_) else ''
            self.group_ids.export(outfile, level, namespaceprefix_, namespacedef_='', name_='group-ids', pretty_print=pretty_print)
        if self.cpc_pickup_indicator is not None:
            namespaceprefix_ = self.cpc_pickup_indicator_nsprefix_ + ':' if (UseCapturedNS_ and self.cpc_pickup_indicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scpc-pickup-indicator>%s</%scpc-pickup-indicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.cpc_pickup_indicator, input_name='cpc-pickup-indicator'), namespaceprefix_ , eol_))
        if self.requested_shipping_point is not None:
            namespaceprefix_ = self.requested_shipping_point_nsprefix_ + ':' if (UseCapturedNS_ and self.requested_shipping_point_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srequested-shipping-point>%s</%srequested-shipping-point>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.requested_shipping_point), input_name='requested-shipping-point')), namespaceprefix_ , eol_))
        if self.shipping_point_id is not None:
            namespaceprefix_ = self.shipping_point_id_nsprefix_ + ':' if (UseCapturedNS_ and self.shipping_point_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshipping-point-id>%s</%sshipping-point-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.shipping_point_id), input_name='shipping-point-id')), namespaceprefix_ , eol_))
        if self.detailed_manifests is not None:
            namespaceprefix_ = self.detailed_manifests_nsprefix_ + ':' if (UseCapturedNS_ and self.detailed_manifests_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdetailed-manifests>%s</%sdetailed-manifests>%s' % (namespaceprefix_ , self.gds_format_boolean(self.detailed_manifests, input_name='detailed-manifests'), namespaceprefix_ , eol_))
        if self.method_of_payment is not None:
            namespaceprefix_ = self.method_of_payment_nsprefix_ + ':' if (UseCapturedNS_ and self.method_of_payment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smethod-of-payment>%s</%smethod-of-payment>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.method_of_payment), input_name='method-of-payment')), namespaceprefix_ , eol_))
        if self.manifest_address is not None:
            namespaceprefix_ = self.manifest_address_nsprefix_ + ':' if (UseCapturedNS_ and self.manifest_address_nsprefix_) else ''
            self.manifest_address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='manifest-address', pretty_print=pretty_print)
        if self.customer_reference is not None:
            namespaceprefix_ = self.customer_reference_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_reference_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-reference>%s</%scustomer-reference>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_reference), input_name='customer-reference')), namespaceprefix_ , eol_))
        if self.excluded_shipments is not None:
            namespaceprefix_ = self.excluded_shipments_nsprefix_ + ':' if (UseCapturedNS_ and self.excluded_shipments_nsprefix_) else ''
            self.excluded_shipments.export(outfile, level, namespaceprefix_, namespacedef_='', name_='excluded-shipments', pretty_print=pretty_print)
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
        if nodeName_ == 'customer-request-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customer_request_id')
            value_ = self.gds_validate_string(value_, node, 'customer_request_id')
            self.customer_request_id = value_
            self.customer_request_id_nsprefix_ = child_.prefix
            # validate type CustomerRequestIdType
            self.validate_CustomerRequestIdType(self.customer_request_id)
        elif nodeName_ == 'group-ids':
            obj_ = GroupIDListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.group_ids = obj_
            obj_.original_tagname_ = 'group-ids'
        elif nodeName_ == 'cpc-pickup-indicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'cpc_pickup_indicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'cpc_pickup_indicator')
            self.cpc_pickup_indicator = ival_
            self.cpc_pickup_indicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'requested-shipping-point':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'requested_shipping_point')
            value_ = self.gds_validate_string(value_, node, 'requested_shipping_point')
            self.requested_shipping_point = value_
            self.requested_shipping_point_nsprefix_ = child_.prefix
        elif nodeName_ == 'shipping-point-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shipping_point_id')
            value_ = self.gds_validate_string(value_, node, 'shipping_point_id')
            self.shipping_point_id = value_
            self.shipping_point_id_nsprefix_ = child_.prefix
        elif nodeName_ == 'detailed-manifests':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'detailed_manifests')
            ival_ = self.gds_validate_boolean(ival_, node, 'detailed_manifests')
            self.detailed_manifests = ival_
            self.detailed_manifests_nsprefix_ = child_.prefix
        elif nodeName_ == 'method-of-payment':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'method_of_payment')
            value_ = self.gds_validate_string(value_, node, 'method_of_payment')
            self.method_of_payment = value_
            self.method_of_payment_nsprefix_ = child_.prefix
        elif nodeName_ == 'manifest-address':
            obj_ = ManifestAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.manifest_address = obj_
            obj_.original_tagname_ = 'manifest-address'
        elif nodeName_ == 'customer-reference':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customer_reference')
            value_ = self.gds_validate_string(value_, node, 'customer_reference')
            self.customer_reference = value_
            self.customer_reference_nsprefix_ = child_.prefix
            # validate type CustomerReferenceType
            self.validate_CustomerReferenceType(self.customer_reference)
        elif nodeName_ == 'excluded-shipments':
            obj_ = ExcludedShipmentsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.excluded_shipments = obj_
            obj_.original_tagname_ = 'excluded-shipments'
# end class ShipmentTransmitSetType


class GroupIDListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, group_id=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if group_id is None:
            self.group_id = []
        else:
            self.group_id = group_id
        self.group_id_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GroupIDListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GroupIDListType.subclass:
            return GroupIDListType.subclass(*args_, **kwargs_)
        else:
            return GroupIDListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_group_id(self):
        return self.group_id
    def set_group_id(self, group_id):
        self.group_id = group_id
    def add_group_id(self, value):
        self.group_id.append(value)
    def insert_group_id_at(self, index, value):
        self.group_id.insert(index, value)
    def replace_group_id_at(self, index, value):
        self.group_id[index] = value
    def validate_GroupIDType(self, value):
        result = True
        # Validate type GroupIDType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on GroupIDType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on GroupIDType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.group_id
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupIDListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GroupIDListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GroupIDListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GroupIDListType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GroupIDListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GroupIDListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupIDListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for group_id_ in self.group_id:
            namespaceprefix_ = self.group_id_nsprefix_ + ':' if (UseCapturedNS_ and self.group_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgroup-id>%s</%sgroup-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(group_id_), input_name='group-id')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'group-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'group_id')
            value_ = self.gds_validate_string(value_, node, 'group_id')
            self.group_id.append(value_)
            self.group_id_nsprefix_ = child_.prefix
            # validate type GroupIDType
            self.validate_GroupIDType(self.group_id[-1])
# end class GroupIDListType


class ExcludedShipmentsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, shipment_id=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if shipment_id is None:
            self.shipment_id = []
        else:
            self.shipment_id = shipment_id
        self.shipment_id_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ExcludedShipmentsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ExcludedShipmentsType.subclass:
            return ExcludedShipmentsType.subclass(*args_, **kwargs_)
        else:
            return ExcludedShipmentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_shipment_id(self):
        return self.shipment_id
    def set_shipment_id(self, shipment_id):
        self.shipment_id = shipment_id
    def add_shipment_id(self, value):
        self.shipment_id.append(value)
    def insert_shipment_id_at(self, index, value):
        self.shipment_id.insert(index, value)
    def replace_shipment_id_at(self, index, value):
        self.shipment_id[index] = value
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
    def _hasContent(self):
        if (
            self.shipment_id
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ExcludedShipmentsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ExcludedShipmentsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ExcludedShipmentsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ExcludedShipmentsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ExcludedShipmentsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ExcludedShipmentsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ExcludedShipmentsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for shipment_id_ in self.shipment_id:
            namespaceprefix_ = self.shipment_id_nsprefix_ + ':' if (UseCapturedNS_ and self.shipment_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshipment-id>%s</%sshipment-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(shipment_id_), input_name='shipment-id')), namespaceprefix_ , eol_))
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
            self.shipment_id.append(value_)
            self.shipment_id_nsprefix_ = child_.prefix
            # validate type ShipmentIDType
            self.validate_ShipmentIDType(self.shipment_id[-1])
# end class ExcludedShipmentsType


class ShipmentsType(GeneratedsSuper):
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
                CurrentSubclassModule_, ShipmentsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentsType.subclass:
            return ShipmentsType.subclass(*args_, **kwargs_)
        else:
            return ShipmentsType(*args_, **kwargs_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentsType', fromsubclass_=False, pretty_print=True):
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
# end class ShipmentsType


class ManifestsType(GeneratedsSuper):
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
                CurrentSubclassModule_, ManifestsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ManifestsType.subclass:
            return ManifestsType.subclass(*args_, **kwargs_)
        else:
            return ManifestsType(*args_, **kwargs_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ManifestsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ManifestsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ManifestsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ManifestsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ManifestsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ManifestsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ManifestsType', fromsubclass_=False, pretty_print=True):
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
# end class ManifestsType


class ManifestType(GeneratedsSuper):
    """customer-request-id -- For future use
    
    """
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, customer_request_id=None, po_number=None, links=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customer_request_id = customer_request_id
        self.validate_CustomerRequestIdType(self.customer_request_id)
        self.customer_request_id_nsprefix_ = None
        self.po_number = po_number
        self.po_number_nsprefix_ = None
        self.links = links
        self.links_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ManifestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ManifestType.subclass:
            return ManifestType.subclass(*args_, **kwargs_)
        else:
            return ManifestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_customer_request_id(self):
        return self.customer_request_id
    def set_customer_request_id(self, customer_request_id):
        self.customer_request_id = customer_request_id
    def get_po_number(self):
        return self.po_number
    def set_po_number(self, po_number):
        self.po_number = po_number
    def get_links(self):
        return self.links
    def set_links(self, links):
        self.links = links
    def validate_CustomerRequestIdType(self, value):
        result = True
        # Validate type CustomerRequestIdType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 35:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CustomerRequestIdType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.customer_request_id is not None or
            self.po_number is not None or
            self.links is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ManifestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ManifestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ManifestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ManifestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ManifestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ManifestType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ManifestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.customer_request_id is not None:
            namespaceprefix_ = self.customer_request_id_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_request_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-request-id>%s</%scustomer-request-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_request_id), input_name='customer-request-id')), namespaceprefix_ , eol_))
        if self.po_number is not None:
            namespaceprefix_ = self.po_number_nsprefix_ + ':' if (UseCapturedNS_ and self.po_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spo-number>%s</%spo-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.po_number), input_name='po-number')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'customer-request-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customer_request_id')
            value_ = self.gds_validate_string(value_, node, 'customer_request_id')
            self.customer_request_id = value_
            self.customer_request_id_nsprefix_ = child_.prefix
            # validate type CustomerRequestIdType
            self.validate_CustomerRequestIdType(self.customer_request_id)
        elif nodeName_ == 'po-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'po_number')
            value_ = self.gds_validate_string(value_, node, 'po_number')
            self.po_number = value_
            self.po_number_nsprefix_ = child_.prefix
        elif nodeName_ == 'links':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'links')
            value_ = self.gds_validate_string(value_, node, 'links')
            self.links = value_
            self.links_nsprefix_ = child_.prefix
# end class ManifestType


class ManifestDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, po_number=None, final_shipping_point=None, shipping_point_name=None, shipping_point_id=None, cpc_pickup_indicator=None, mailed_by_customer=None, mailed_on_behalf_of=None, paid_by_customer=None, customer_ref=None, manifest_date=None, manifest_time=None, contract_id=None, method_of_payment=None, cc_receipt_details=None, supplier_account_receipt_details=None, manifest_pricing_info=None, manifest_address=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.po_number = po_number
        self.po_number_nsprefix_ = None
        self.final_shipping_point = final_shipping_point
        self.final_shipping_point_nsprefix_ = None
        self.shipping_point_name = shipping_point_name
        self.validate_shipping_point_nameType(self.shipping_point_name)
        self.shipping_point_name_nsprefix_ = None
        self.shipping_point_id = shipping_point_id
        self.shipping_point_id_nsprefix_ = None
        self.cpc_pickup_indicator = cpc_pickup_indicator
        self.cpc_pickup_indicator_nsprefix_ = None
        self.mailed_by_customer = mailed_by_customer
        self.mailed_by_customer_nsprefix_ = None
        self.mailed_on_behalf_of = mailed_on_behalf_of
        self.mailed_on_behalf_of_nsprefix_ = None
        self.paid_by_customer = paid_by_customer
        self.paid_by_customer_nsprefix_ = None
        self.customer_ref = customer_ref
        self.customer_ref_nsprefix_ = None
        if isinstance(manifest_date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(manifest_date, '%Y-%m-%d').date()
        else:
            initvalue_ = manifest_date
        self.manifest_date = initvalue_
        self.manifest_date_nsprefix_ = None
        self.manifest_time = manifest_time
        self.validate_manifest_timeType(self.manifest_time)
        self.manifest_time_nsprefix_ = None
        self.contract_id = contract_id
        self.contract_id_nsprefix_ = None
        self.method_of_payment = method_of_payment
        self.method_of_payment_nsprefix_ = None
        self.cc_receipt_details = cc_receipt_details
        self.cc_receipt_details_nsprefix_ = None
        self.supplier_account_receipt_details = supplier_account_receipt_details
        self.supplier_account_receipt_details_nsprefix_ = None
        self.manifest_pricing_info = manifest_pricing_info
        self.manifest_pricing_info_nsprefix_ = None
        self.manifest_address = manifest_address
        self.manifest_address_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ManifestDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ManifestDetailsType.subclass:
            return ManifestDetailsType.subclass(*args_, **kwargs_)
        else:
            return ManifestDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_po_number(self):
        return self.po_number
    def set_po_number(self, po_number):
        self.po_number = po_number
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
    def get_cpc_pickup_indicator(self):
        return self.cpc_pickup_indicator
    def set_cpc_pickup_indicator(self, cpc_pickup_indicator):
        self.cpc_pickup_indicator = cpc_pickup_indicator
    def get_mailed_by_customer(self):
        return self.mailed_by_customer
    def set_mailed_by_customer(self, mailed_by_customer):
        self.mailed_by_customer = mailed_by_customer
    def get_mailed_on_behalf_of(self):
        return self.mailed_on_behalf_of
    def set_mailed_on_behalf_of(self, mailed_on_behalf_of):
        self.mailed_on_behalf_of = mailed_on_behalf_of
    def get_paid_by_customer(self):
        return self.paid_by_customer
    def set_paid_by_customer(self, paid_by_customer):
        self.paid_by_customer = paid_by_customer
    def get_customer_ref(self):
        return self.customer_ref
    def set_customer_ref(self, customer_ref):
        self.customer_ref = customer_ref
    def get_manifest_date(self):
        return self.manifest_date
    def set_manifest_date(self, manifest_date):
        self.manifest_date = manifest_date
    def get_manifest_time(self):
        return self.manifest_time
    def set_manifest_time(self, manifest_time):
        self.manifest_time = manifest_time
    def get_contract_id(self):
        return self.contract_id
    def set_contract_id(self, contract_id):
        self.contract_id = contract_id
    def get_method_of_payment(self):
        return self.method_of_payment
    def set_method_of_payment(self, method_of_payment):
        self.method_of_payment = method_of_payment
    def get_cc_receipt_details(self):
        return self.cc_receipt_details
    def set_cc_receipt_details(self, cc_receipt_details):
        self.cc_receipt_details = cc_receipt_details
    def get_supplier_account_receipt_details(self):
        return self.supplier_account_receipt_details
    def set_supplier_account_receipt_details(self, supplier_account_receipt_details):
        self.supplier_account_receipt_details = supplier_account_receipt_details
    def get_manifest_pricing_info(self):
        return self.manifest_pricing_info
    def set_manifest_pricing_info(self, manifest_pricing_info):
        self.manifest_pricing_info = manifest_pricing_info
    def get_manifest_address(self):
        return self.manifest_address
    def set_manifest_address(self, manifest_address):
        self.manifest_address = manifest_address
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
    def validate_manifest_timeType(self, value):
        result = True
        # Validate type manifest-timeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_manifest_timeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_manifest_timeType_patterns_, ))
                result = False
        return result
    validate_manifest_timeType_patterns_ = [['^(\\d{2}:\\d{2} [a-zA-Z ]+)$']]
    def _hasContent(self):
        if (
            self.po_number is not None or
            self.final_shipping_point is not None or
            self.shipping_point_name is not None or
            self.shipping_point_id is not None or
            self.cpc_pickup_indicator is not None or
            self.mailed_by_customer is not None or
            self.mailed_on_behalf_of is not None or
            self.paid_by_customer is not None or
            self.customer_ref is not None or
            self.manifest_date is not None or
            self.manifest_time is not None or
            self.contract_id is not None or
            self.method_of_payment is not None or
            self.cc_receipt_details is not None or
            self.supplier_account_receipt_details is not None or
            self.manifest_pricing_info is not None or
            self.manifest_address is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ManifestDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ManifestDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ManifestDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ManifestDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ManifestDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ManifestDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ManifestDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.po_number is not None:
            namespaceprefix_ = self.po_number_nsprefix_ + ':' if (UseCapturedNS_ and self.po_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spo-number>%s</%spo-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.po_number), input_name='po-number')), namespaceprefix_ , eol_))
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
        if self.cpc_pickup_indicator is not None:
            namespaceprefix_ = self.cpc_pickup_indicator_nsprefix_ + ':' if (UseCapturedNS_ and self.cpc_pickup_indicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scpc-pickup-indicator>%s</%scpc-pickup-indicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.cpc_pickup_indicator, input_name='cpc-pickup-indicator'), namespaceprefix_ , eol_))
        if self.mailed_by_customer is not None:
            namespaceprefix_ = self.mailed_by_customer_nsprefix_ + ':' if (UseCapturedNS_ and self.mailed_by_customer_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smailed-by-customer>%s</%smailed-by-customer>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.mailed_by_customer), input_name='mailed-by-customer')), namespaceprefix_ , eol_))
        if self.mailed_on_behalf_of is not None:
            namespaceprefix_ = self.mailed_on_behalf_of_nsprefix_ + ':' if (UseCapturedNS_ and self.mailed_on_behalf_of_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smailed-on-behalf-of>%s</%smailed-on-behalf-of>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.mailed_on_behalf_of), input_name='mailed-on-behalf-of')), namespaceprefix_ , eol_))
        if self.paid_by_customer is not None:
            namespaceprefix_ = self.paid_by_customer_nsprefix_ + ':' if (UseCapturedNS_ and self.paid_by_customer_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spaid-by-customer>%s</%spaid-by-customer>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.paid_by_customer), input_name='paid-by-customer')), namespaceprefix_ , eol_))
        if self.customer_ref is not None:
            namespaceprefix_ = self.customer_ref_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_ref_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-ref>%s</%scustomer-ref>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_ref), input_name='customer-ref')), namespaceprefix_ , eol_))
        if self.manifest_date is not None:
            namespaceprefix_ = self.manifest_date_nsprefix_ + ':' if (UseCapturedNS_ and self.manifest_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smanifest-date>%s</%smanifest-date>%s' % (namespaceprefix_ , self.gds_format_date(self.manifest_date, input_name='manifest-date'), namespaceprefix_ , eol_))
        if self.manifest_time is not None:
            namespaceprefix_ = self.manifest_time_nsprefix_ + ':' if (UseCapturedNS_ and self.manifest_time_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smanifest-time>%s</%smanifest-time>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.manifest_time), input_name='manifest-time')), namespaceprefix_ , eol_))
        if self.contract_id is not None:
            namespaceprefix_ = self.contract_id_nsprefix_ + ':' if (UseCapturedNS_ and self.contract_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontract-id>%s</%scontract-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contract_id), input_name='contract-id')), namespaceprefix_ , eol_))
        if self.method_of_payment is not None:
            namespaceprefix_ = self.method_of_payment_nsprefix_ + ':' if (UseCapturedNS_ and self.method_of_payment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smethod-of-payment>%s</%smethod-of-payment>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.method_of_payment), input_name='method-of-payment')), namespaceprefix_ , eol_))
        if self.cc_receipt_details is not None:
            namespaceprefix_ = self.cc_receipt_details_nsprefix_ + ':' if (UseCapturedNS_ and self.cc_receipt_details_nsprefix_) else ''
            self.cc_receipt_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='cc-receipt-details', pretty_print=pretty_print)
        if self.supplier_account_receipt_details is not None:
            namespaceprefix_ = self.supplier_account_receipt_details_nsprefix_ + ':' if (UseCapturedNS_ and self.supplier_account_receipt_details_nsprefix_) else ''
            self.supplier_account_receipt_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='supplier-account-receipt-details', pretty_print=pretty_print)
        if self.manifest_pricing_info is not None:
            namespaceprefix_ = self.manifest_pricing_info_nsprefix_ + ':' if (UseCapturedNS_ and self.manifest_pricing_info_nsprefix_) else ''
            self.manifest_pricing_info.export(outfile, level, namespaceprefix_, namespacedef_='', name_='manifest-pricing-info', pretty_print=pretty_print)
        if self.manifest_address is not None:
            namespaceprefix_ = self.manifest_address_nsprefix_ + ':' if (UseCapturedNS_ and self.manifest_address_nsprefix_) else ''
            self.manifest_address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='manifest-address', pretty_print=pretty_print)
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
        if nodeName_ == 'po-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'po_number')
            value_ = self.gds_validate_string(value_, node, 'po_number')
            self.po_number = value_
            self.po_number_nsprefix_ = child_.prefix
        elif nodeName_ == 'final-shipping-point':
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
        elif nodeName_ == 'cpc-pickup-indicator':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'cpc_pickup_indicator')
            ival_ = self.gds_validate_boolean(ival_, node, 'cpc_pickup_indicator')
            self.cpc_pickup_indicator = ival_
            self.cpc_pickup_indicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'mailed-by-customer':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mailed_by_customer')
            value_ = self.gds_validate_string(value_, node, 'mailed_by_customer')
            self.mailed_by_customer = value_
            self.mailed_by_customer_nsprefix_ = child_.prefix
        elif nodeName_ == 'mailed-on-behalf-of':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mailed_on_behalf_of')
            value_ = self.gds_validate_string(value_, node, 'mailed_on_behalf_of')
            self.mailed_on_behalf_of = value_
            self.mailed_on_behalf_of_nsprefix_ = child_.prefix
        elif nodeName_ == 'paid-by-customer':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'paid_by_customer')
            value_ = self.gds_validate_string(value_, node, 'paid_by_customer')
            self.paid_by_customer = value_
            self.paid_by_customer_nsprefix_ = child_.prefix
        elif nodeName_ == 'customer-ref':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customer_ref')
            value_ = self.gds_validate_string(value_, node, 'customer_ref')
            self.customer_ref = value_
            self.customer_ref_nsprefix_ = child_.prefix
        elif nodeName_ == 'manifest-date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.manifest_date = dval_
            self.manifest_date_nsprefix_ = child_.prefix
        elif nodeName_ == 'manifest-time':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'manifest_time')
            value_ = self.gds_validate_string(value_, node, 'manifest_time')
            self.manifest_time = value_
            self.manifest_time_nsprefix_ = child_.prefix
            # validate type manifest-timeType
            self.validate_manifest_timeType(self.manifest_time)
        elif nodeName_ == 'contract-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contract_id')
            value_ = self.gds_validate_string(value_, node, 'contract_id')
            self.contract_id = value_
            self.contract_id_nsprefix_ = child_.prefix
        elif nodeName_ == 'method-of-payment':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'method_of_payment')
            value_ = self.gds_validate_string(value_, node, 'method_of_payment')
            self.method_of_payment = value_
            self.method_of_payment_nsprefix_ = child_.prefix
        elif nodeName_ == 'cc-receipt-details':
            obj_ = cc_receipt_detailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.cc_receipt_details = obj_
            obj_.original_tagname_ = 'cc-receipt-details'
        elif nodeName_ == 'supplier-account-receipt-details':
            obj_ = supplier_account_receipt_detailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.supplier_account_receipt_details = obj_
            obj_.original_tagname_ = 'supplier-account-receipt-details'
        elif nodeName_ == 'manifest-pricing-info':
            obj_ = ManifestPricingInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.manifest_pricing_info = obj_
            obj_.original_tagname_ = 'manifest-pricing-info'
        elif nodeName_ == 'manifest-address':
            obj_ = ManifestAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.manifest_address = obj_
            obj_.original_tagname_ = 'manifest-address'
# end class ManifestDetailsType


class ManifestPricingInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, base_cost=None, automation_discount=None, options_and_surcharges=None, gst=None, pst=None, hst=None, total_due_cpc=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.base_cost = base_cost
        self.base_cost_nsprefix_ = None
        self.automation_discount = automation_discount
        self.automation_discount_nsprefix_ = None
        self.options_and_surcharges = options_and_surcharges
        self.options_and_surcharges_nsprefix_ = None
        self.gst = gst
        self.gst_nsprefix_ = None
        self.pst = pst
        self.pst_nsprefix_ = None
        self.hst = hst
        self.hst_nsprefix_ = None
        self.total_due_cpc = total_due_cpc
        self.total_due_cpc_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ManifestPricingInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ManifestPricingInfoType.subclass:
            return ManifestPricingInfoType.subclass(*args_, **kwargs_)
        else:
            return ManifestPricingInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_base_cost(self):
        return self.base_cost
    def set_base_cost(self, base_cost):
        self.base_cost = base_cost
    def get_automation_discount(self):
        return self.automation_discount
    def set_automation_discount(self, automation_discount):
        self.automation_discount = automation_discount
    def get_options_and_surcharges(self):
        return self.options_and_surcharges
    def set_options_and_surcharges(self, options_and_surcharges):
        self.options_and_surcharges = options_and_surcharges
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
    def get_total_due_cpc(self):
        return self.total_due_cpc
    def set_total_due_cpc(self, total_due_cpc):
        self.total_due_cpc = total_due_cpc
    def _hasContent(self):
        if (
            self.base_cost is not None or
            self.automation_discount is not None or
            self.options_and_surcharges is not None or
            self.gst is not None or
            self.pst is not None or
            self.hst is not None or
            self.total_due_cpc is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ManifestPricingInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ManifestPricingInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ManifestPricingInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ManifestPricingInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ManifestPricingInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ManifestPricingInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ManifestPricingInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.base_cost is not None:
            namespaceprefix_ = self.base_cost_nsprefix_ + ':' if (UseCapturedNS_ and self.base_cost_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbase-cost>%s</%sbase-cost>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.base_cost), input_name='base-cost')), namespaceprefix_ , eol_))
        if self.automation_discount is not None:
            namespaceprefix_ = self.automation_discount_nsprefix_ + ':' if (UseCapturedNS_ and self.automation_discount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sautomation-discount>%s</%sautomation-discount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.automation_discount), input_name='automation-discount')), namespaceprefix_ , eol_))
        if self.options_and_surcharges is not None:
            namespaceprefix_ = self.options_and_surcharges_nsprefix_ + ':' if (UseCapturedNS_ and self.options_and_surcharges_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soptions-and-surcharges>%s</%soptions-and-surcharges>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.options_and_surcharges), input_name='options-and-surcharges')), namespaceprefix_ , eol_))
        if self.gst is not None:
            namespaceprefix_ = self.gst_nsprefix_ + ':' if (UseCapturedNS_ and self.gst_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgst>%s</%sgst>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.gst), input_name='gst')), namespaceprefix_ , eol_))
        if self.pst is not None:
            namespaceprefix_ = self.pst_nsprefix_ + ':' if (UseCapturedNS_ and self.pst_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spst>%s</%spst>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pst), input_name='pst')), namespaceprefix_ , eol_))
        if self.hst is not None:
            namespaceprefix_ = self.hst_nsprefix_ + ':' if (UseCapturedNS_ and self.hst_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shst>%s</%shst>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.hst), input_name='hst')), namespaceprefix_ , eol_))
        if self.total_due_cpc is not None:
            namespaceprefix_ = self.total_due_cpc_nsprefix_ + ':' if (UseCapturedNS_ and self.total_due_cpc_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stotal-due-cpc>%s</%stotal-due-cpc>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.total_due_cpc), input_name='total-due-cpc')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'base-cost':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'base_cost')
            value_ = self.gds_validate_string(value_, node, 'base_cost')
            self.base_cost = value_
            self.base_cost_nsprefix_ = child_.prefix
        elif nodeName_ == 'automation-discount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'automation_discount')
            value_ = self.gds_validate_string(value_, node, 'automation_discount')
            self.automation_discount = value_
            self.automation_discount_nsprefix_ = child_.prefix
        elif nodeName_ == 'options-and-surcharges':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'options_and_surcharges')
            value_ = self.gds_validate_string(value_, node, 'options_and_surcharges')
            self.options_and_surcharges = value_
            self.options_and_surcharges_nsprefix_ = child_.prefix
        elif nodeName_ == 'gst':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'gst')
            value_ = self.gds_validate_string(value_, node, 'gst')
            self.gst = value_
            self.gst_nsprefix_ = child_.prefix
        elif nodeName_ == 'pst':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pst')
            value_ = self.gds_validate_string(value_, node, 'pst')
            self.pst = value_
            self.pst_nsprefix_ = child_.prefix
        elif nodeName_ == 'hst':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'hst')
            value_ = self.gds_validate_string(value_, node, 'hst')
            self.hst = value_
            self.hst_nsprefix_ = child_.prefix
        elif nodeName_ == 'total-due-cpc':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'total_due_cpc')
            value_ = self.gds_validate_string(value_, node, 'total_due_cpc')
            self.total_due_cpc = value_
            self.total_due_cpc_nsprefix_ = child_.prefix
# end class ManifestPricingInfoType


class ManifestAddressType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, manifest_company=None, manifest_name=None, phone_number=None, address_details=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.manifest_company = manifest_company
        self.validate_manifest_companyType(self.manifest_company)
        self.manifest_company_nsprefix_ = None
        self.manifest_name = manifest_name
        self.validate_manifest_nameType(self.manifest_name)
        self.manifest_name_nsprefix_ = None
        self.phone_number = phone_number
        self.phone_number_nsprefix_ = None
        self.address_details = address_details
        self.address_details_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ManifestAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ManifestAddressType.subclass:
            return ManifestAddressType.subclass(*args_, **kwargs_)
        else:
            return ManifestAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_manifest_company(self):
        return self.manifest_company
    def set_manifest_company(self, manifest_company):
        self.manifest_company = manifest_company
    def get_manifest_name(self):
        return self.manifest_name
    def set_manifest_name(self, manifest_name):
        self.manifest_name = manifest_name
    def get_phone_number(self):
        return self.phone_number
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    def get_address_details(self):
        return self.address_details
    def set_address_details(self, address_details):
        self.address_details = address_details
    def validate_manifest_companyType(self, value):
        result = True
        # Validate type manifest-companyType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on manifest-companyType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on manifest-companyType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_manifest_nameType(self, value):
        result = True
        # Validate type manifest-nameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on manifest-nameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on manifest-nameType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.manifest_company is not None or
            self.manifest_name is not None or
            self.phone_number is not None or
            self.address_details is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ManifestAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ManifestAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ManifestAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ManifestAddressType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ManifestAddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ManifestAddressType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ManifestAddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.manifest_company is not None:
            namespaceprefix_ = self.manifest_company_nsprefix_ + ':' if (UseCapturedNS_ and self.manifest_company_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smanifest-company>%s</%smanifest-company>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.manifest_company), input_name='manifest-company')), namespaceprefix_ , eol_))
        if self.manifest_name is not None:
            namespaceprefix_ = self.manifest_name_nsprefix_ + ':' if (UseCapturedNS_ and self.manifest_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smanifest-name>%s</%smanifest-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.manifest_name), input_name='manifest-name')), namespaceprefix_ , eol_))
        if self.phone_number is not None:
            namespaceprefix_ = self.phone_number_nsprefix_ + ':' if (UseCapturedNS_ and self.phone_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sphone-number>%s</%sphone-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.phone_number), input_name='phone-number')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'manifest-company':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'manifest_company')
            value_ = self.gds_validate_string(value_, node, 'manifest_company')
            self.manifest_company = value_
            self.manifest_company_nsprefix_ = child_.prefix
            # validate type manifest-companyType
            self.validate_manifest_companyType(self.manifest_company)
        elif nodeName_ == 'manifest-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'manifest_name')
            value_ = self.gds_validate_string(value_, node, 'manifest_name')
            self.manifest_name = value_
            self.manifest_name_nsprefix_ = child_.prefix
            # validate type manifest-nameType
            self.validate_manifest_nameType(self.manifest_name)
        elif nodeName_ == 'phone-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'phone_number')
            value_ = self.gds_validate_string(value_, node, 'phone_number')
            self.phone_number = value_
            self.phone_number_nsprefix_ = child_.prefix
        elif nodeName_ == 'address-details':
            obj_ = AddressDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address_details = obj_
            obj_.original_tagname_ = 'address-details'
# end class ManifestAddressType


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
        self.validate_address_line_1Type(self.address_line_1)
        self.address_line_1_nsprefix_ = None
        self.address_line_2 = address_line_2
        self.validate_address_line_2Type(self.address_line_2)
        self.address_line_2_nsprefix_ = None
        self.city = city
        self.validate_cityType(self.city)
        self.city_nsprefix_ = None
        self.prov_state = prov_state
        self.validate_prov_stateType(self.prov_state)
        self.prov_state_nsprefix_ = None
        self.country_code = country_code
        self.validate_country_codeType(self.country_code)
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
    def validate_prov_stateType(self, value):
        result = True
        # Validate type prov-stateType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on prov-stateType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on prov-stateType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_country_codeType(self, value):
        result = True
        # Validate type country-codeType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['CA', 'US']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on country-codeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type prov-stateType
            self.validate_prov_stateType(self.prov_state)
        elif nodeName_ == 'country-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'country_code')
            value_ = self.gds_validate_string(value_, node, 'country_code')
            self.country_code = value_
            self.country_code_nsprefix_ = child_.prefix
            # validate type country-codeType
            self.validate_country_codeType(self.country_code)
        elif nodeName_ == 'postal-zip-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postal_zip_code')
            value_ = self.gds_validate_string(value_, node, 'postal_zip_code')
            self.postal_zip_code = value_
            self.postal_zip_code_nsprefix_ = child_.prefix
# end class AddressDetailsType


class cc_receipt_detailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, merchant_name=None, merchant_url=None, name_on_card=None, auth_code=None, auth_timestamp=None, card_type=None, currency=None, transaction_type=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.merchant_name = merchant_name
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
    def get_currency(self):
        return self.currency
    def set_currency(self, currency):
        self.currency = currency
    def get_transaction_type(self):
        return self.transaction_type
    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type
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


class supplier_account_receipt_detailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, merchant_name=None, merchant_url=None, auth_code=None, auth_timestamp=None, supplier_id=None, currency=None, transaction_type=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.merchant_name = merchant_name
        self.validate_merchant_nameType(self.merchant_name)
        self.merchant_name_nsprefix_ = None
        self.merchant_url = merchant_url
        self.validate_merchant_urlType1(self.merchant_url)
        self.merchant_url_nsprefix_ = None
        self.auth_code = auth_code
        self.auth_code_nsprefix_ = None
        if isinstance(auth_timestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(auth_timestamp, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = auth_timestamp
        self.auth_timestamp = initvalue_
        self.auth_timestamp_nsprefix_ = None
        self.supplier_id = supplier_id
        self.supplier_id_nsprefix_ = None
        self.currency = currency
        self.currency_nsprefix_ = None
        self.transaction_type = transaction_type
        self.validate_transaction_typeType2(self.transaction_type)
        self.transaction_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, supplier_account_receipt_detailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if supplier_account_receipt_detailsType.subclass:
            return supplier_account_receipt_detailsType.subclass(*args_, **kwargs_)
        else:
            return supplier_account_receipt_detailsType(*args_, **kwargs_)
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
    def get_auth_code(self):
        return self.auth_code
    def set_auth_code(self, auth_code):
        self.auth_code = auth_code
    def get_auth_timestamp(self):
        return self.auth_timestamp
    def set_auth_timestamp(self, auth_timestamp):
        self.auth_timestamp = auth_timestamp
    def get_supplier_id(self):
        return self.supplier_id
    def set_supplier_id(self, supplier_id):
        self.supplier_id = supplier_id
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
    def validate_merchant_urlType1(self, value):
        result = True
        # Validate type merchant-urlType1, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchant-urlType1' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_transaction_typeType2(self, value):
        result = True
        # Validate type transaction-typeType2, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on transaction-typeType2' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.merchant_name is not None or
            self.merchant_url is not None or
            self.auth_code is not None or
            self.auth_timestamp is not None or
            self.supplier_id is not None or
            self.currency is not None or
            self.transaction_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='supplier-account-receipt-detailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('supplier-account-receipt-detailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'supplier-account-receipt-detailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='supplier-account-receipt-detailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='supplier-account-receipt-detailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='supplier-account-receipt-detailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='supplier-account-receipt-detailsType', fromsubclass_=False, pretty_print=True):
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
        if self.auth_code is not None:
            namespaceprefix_ = self.auth_code_nsprefix_ + ':' if (UseCapturedNS_ and self.auth_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauth-code>%s</%sauth-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.auth_code), input_name='auth-code')), namespaceprefix_ , eol_))
        if self.auth_timestamp is not None:
            namespaceprefix_ = self.auth_timestamp_nsprefix_ + ':' if (UseCapturedNS_ and self.auth_timestamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauth-timestamp>%s</%sauth-timestamp>%s' % (namespaceprefix_ , self.gds_format_datetime(self.auth_timestamp, input_name='auth-timestamp'), namespaceprefix_ , eol_))
        if self.supplier_id is not None:
            namespaceprefix_ = self.supplier_id_nsprefix_ + ':' if (UseCapturedNS_ and self.supplier_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplier-id>%s</%ssupplier-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.supplier_id), input_name='supplier-id')), namespaceprefix_ , eol_))
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
            # validate type merchant-urlType1
            self.validate_merchant_urlType1(self.merchant_url)
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
        elif nodeName_ == 'supplier-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplier_id')
            value_ = self.gds_validate_string(value_, node, 'supplier_id')
            self.supplier_id = value_
            self.supplier_id_nsprefix_ = child_.prefix
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
            # validate type transaction-typeType2
            self.validate_transaction_typeType2(self.transaction_type)
# end class supplier_account_receipt_detailsType


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
        rootTag = 'ShipmentTransmitSetType'
        rootClass = ShipmentTransmitSetType
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
        rootTag = 'ShipmentTransmitSetType'
        rootClass = ShipmentTransmitSetType
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
        rootTag = 'ShipmentTransmitSetType'
        rootClass = ShipmentTransmitSetType
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
        rootTag = 'ShipmentTransmitSetType'
        rootClass = ShipmentTransmitSetType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from manifest import *\n\n')
        sys.stdout.write('import manifest as model_\n\n')
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
NamespaceToDefMappings_ = {'http://www.canadapost.ca/ws/manifest-v8': [('GroupIDType',
                                              './schemas/manifest.xsd',
                                              'ST'),
                                             ('ShipmentIDType',
                                              './schemas/manifest.xsd',
                                              'ST'),
                                             ('CustomerReferenceType',
                                              './schemas/manifest.xsd',
                                              'ST'),
                                             ('CustomerRequestIdType',
                                              './schemas/manifest.xsd',
                                              'ST'),
                                             ('ShipmentTransmitSetType',
                                              './schemas/manifest.xsd',
                                              'CT'),
                                             ('GroupIDListType',
                                              './schemas/manifest.xsd',
                                              'CT'),
                                             ('ExcludedShipmentsType',
                                              './schemas/manifest.xsd',
                                              'CT'),
                                             ('ShipmentsType',
                                              './schemas/manifest.xsd',
                                              'CT'),
                                             ('ManifestsType',
                                              './schemas/manifest.xsd',
                                              'CT'),
                                             ('ManifestType',
                                              './schemas/manifest.xsd',
                                              'CT'),
                                             ('ManifestDetailsType',
                                              './schemas/manifest.xsd',
                                              'CT'),
                                             ('ManifestPricingInfoType',
                                              './schemas/manifest.xsd',
                                              'CT'),
                                             ('ManifestAddressType',
                                              './schemas/manifest.xsd',
                                              'CT'),
                                             ('AddressDetailsType',
                                              './schemas/manifest.xsd',
                                              'CT')]}

__all__ = [
    "AddressDetailsType",
    "ExcludedShipmentsType",
    "GroupIDListType",
    "ManifestAddressType",
    "ManifestDetailsType",
    "ManifestPricingInfoType",
    "ManifestType",
    "ManifestsType",
    "ShipmentTransmitSetType",
    "ShipmentsType",
    "cc_receipt_detailsType",
    "supplier_account_receipt_detailsType"
]
