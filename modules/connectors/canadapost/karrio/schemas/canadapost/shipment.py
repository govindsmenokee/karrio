#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Jul 14 15:39:45 2021 by generateDS.py version 2.39.2.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './canadapost_lib/shipment.py')
#
# Command line arguments:
#   ./schemas/shipment.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-carriers/.venv/karrio-carriers/bin/generateDS --no-namespace-defs -o "./canadapost_lib/shipment.py" ./schemas/shipment.xsd
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
    GROUP='group'
    SHIPMENT='shipment'
    PRICE='price'
    LABEL='label'
    RETURN_LABEL='returnLabel'
    COMMERCIAL_INVOICE='commercialInvoice'
    RECEIPT='receipt'
    REFUND='refund'


class encodingType(str, Enum):
    PDF='PDF'
    ZPL='ZPL'


class output_formatType(str, Enum):
    _8_5_X_11='8.5x11'
    _4_X_6='4x6'


class GroupsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, group=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if group is None:
            self.group = []
        else:
            self.group = group
        self.group_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GroupsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GroupsType.subclass:
            return GroupsType.subclass(*args_, **kwargs_)
        else:
            return GroupsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_group(self):
        return self.group
    def set_group(self, group):
        self.group = group
    def add_group(self, value):
        self.group.append(value)
    def insert_group_at(self, index, value):
        self.group.insert(index, value)
    def replace_group_at(self, index, value):
        self.group[index] = value
    def _hasContent(self):
        if (
            self.group
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GroupsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GroupsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GroupsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GroupsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GroupsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for group_ in self.group:
            namespaceprefix_ = self.group_nsprefix_ + ':' if (UseCapturedNS_ and self.group_nsprefix_) else ''
            group_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='group', pretty_print=pretty_print)
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
        if nodeName_ == 'group':
            obj_ = GroupType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.group.append(obj_)
            obj_.original_tagname_ = 'group'
# end class GroupsType


class GroupType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, group_id=None, link=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.group_id = group_id
        self.group_id_nsprefix_ = None
        self.link = link
        self.link_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GroupType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GroupType.subclass:
            return GroupType.subclass(*args_, **kwargs_)
        else:
            return GroupType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_group_id(self):
        return self.group_id
    def set_group_id(self, group_id):
        self.group_id = group_id
    def get_link(self):
        return self.link
    def set_link(self, link):
        self.link = link
    def _hasContent(self):
        if (
            self.group_id is not None or
            self.link is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GroupType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GroupType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GroupType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GroupType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GroupType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.group_id is not None:
            namespaceprefix_ = self.group_id_nsprefix_ + ':' if (UseCapturedNS_ and self.group_id_nsprefix_) else ''
            self.group_id.export(outfile, level, namespaceprefix_, namespacedef_='', name_='group-id', pretty_print=pretty_print)
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
        if nodeName_ == 'group-id':
            obj_ = GroupIDType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.group_id = obj_
            obj_.original_tagname_ = 'group-id'
        elif nodeName_ == 'link':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'link')
            value_ = self.gds_validate_string(value_, node, 'link')
            self.link = value_
            self.link_nsprefix_ = child_.prefix
# end class GroupType


class ShipmentPriceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service_code=None, base_amount=None, priced_options=None, adjustments=None, pre_tax_amount=None, gst_amount=None, pst_amount=None, hst_amount=None, due_amount=None, service_standard=None, rated_weight=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.service_code = service_code
        self.service_code_nsprefix_ = None
        self.base_amount = base_amount
        self.base_amount_nsprefix_ = None
        self.priced_options = priced_options
        self.priced_options_nsprefix_ = None
        self.adjustments = adjustments
        self.adjustments_nsprefix_ = None
        self.pre_tax_amount = pre_tax_amount
        self.pre_tax_amount_nsprefix_ = None
        self.gst_amount = gst_amount
        self.gst_amount_nsprefix_ = None
        self.pst_amount = pst_amount
        self.pst_amount_nsprefix_ = None
        self.hst_amount = hst_amount
        self.hst_amount_nsprefix_ = None
        self.due_amount = due_amount
        self.due_amount_nsprefix_ = None
        self.service_standard = service_standard
        self.service_standard_nsprefix_ = None
        self.rated_weight = rated_weight
        self.validate_rated_weightType(self.rated_weight)
        self.rated_weight_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentPriceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentPriceType.subclass:
            return ShipmentPriceType.subclass(*args_, **kwargs_)
        else:
            return ShipmentPriceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_service_code(self):
        return self.service_code
    def set_service_code(self, service_code):
        self.service_code = service_code
    def get_base_amount(self):
        return self.base_amount
    def set_base_amount(self, base_amount):
        self.base_amount = base_amount
    def get_priced_options(self):
        return self.priced_options
    def set_priced_options(self, priced_options):
        self.priced_options = priced_options
    def get_adjustments(self):
        return self.adjustments
    def set_adjustments(self, adjustments):
        self.adjustments = adjustments
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
    def get_due_amount(self):
        return self.due_amount
    def set_due_amount(self, due_amount):
        self.due_amount = due_amount
    def get_service_standard(self):
        return self.service_standard
    def set_service_standard(self, service_standard):
        self.service_standard = service_standard
    def get_rated_weight(self):
        return self.rated_weight
    def set_rated_weight(self, rated_weight):
        self.rated_weight = rated_weight
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
            self.service_code is not None or
            self.base_amount is not None or
            self.priced_options is not None or
            self.adjustments is not None or
            self.pre_tax_amount is not None or
            self.gst_amount is not None or
            self.pst_amount is not None or
            self.hst_amount is not None or
            self.due_amount is not None or
            self.service_standard is not None or
            self.rated_weight is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentPriceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentPriceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentPriceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentPriceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentPriceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentPriceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentPriceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.service_code is not None:
            namespaceprefix_ = self.service_code_nsprefix_ + ':' if (UseCapturedNS_ and self.service_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-code>%s</%sservice-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_code), input_name='service-code')), namespaceprefix_ , eol_))
        if self.base_amount is not None:
            namespaceprefix_ = self.base_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.base_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbase-amount>%s</%sbase-amount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.base_amount), input_name='base-amount')), namespaceprefix_ , eol_))
        if self.priced_options is not None:
            namespaceprefix_ = self.priced_options_nsprefix_ + ':' if (UseCapturedNS_ and self.priced_options_nsprefix_) else ''
            self.priced_options.export(outfile, level, namespaceprefix_, namespacedef_='', name_='priced-options', pretty_print=pretty_print)
        if self.adjustments is not None:
            namespaceprefix_ = self.adjustments_nsprefix_ + ':' if (UseCapturedNS_ and self.adjustments_nsprefix_) else ''
            self.adjustments.export(outfile, level, namespaceprefix_, namespacedef_='', name_='adjustments', pretty_print=pretty_print)
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
        if self.due_amount is not None:
            namespaceprefix_ = self.due_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.due_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdue-amount>%s</%sdue-amount>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.due_amount), input_name='due-amount')), namespaceprefix_ , eol_))
        if self.service_standard is not None:
            namespaceprefix_ = self.service_standard_nsprefix_ + ':' if (UseCapturedNS_ and self.service_standard_nsprefix_) else ''
            self.service_standard.export(outfile, level, namespaceprefix_, namespacedef_='', name_='service-standard', pretty_print=pretty_print)
        if self.rated_weight is not None:
            namespaceprefix_ = self.rated_weight_nsprefix_ + ':' if (UseCapturedNS_ and self.rated_weight_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srated-weight>%s</%srated-weight>%s' % (namespaceprefix_ , self.gds_format_decimal(self.rated_weight, input_name='rated-weight'), namespaceprefix_ , eol_))
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
        elif nodeName_ == 'base-amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'base_amount')
            value_ = self.gds_validate_string(value_, node, 'base_amount')
            self.base_amount = value_
            self.base_amount_nsprefix_ = child_.prefix
        elif nodeName_ == 'priced-options':
            obj_ = PricedOptionsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.priced_options = obj_
            obj_.original_tagname_ = 'priced-options'
        elif nodeName_ == 'adjustments':
            obj_ = AdjustmentsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.adjustments = obj_
            obj_.original_tagname_ = 'adjustments'
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
        elif nodeName_ == 'due-amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'due_amount')
            value_ = self.gds_validate_string(value_, node, 'due_amount')
            self.due_amount = value_
            self.due_amount_nsprefix_ = child_.prefix
        elif nodeName_ == 'service-standard':
            obj_ = ServiceStandardType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.service_standard = obj_
            obj_.original_tagname_ = 'service-standard'
        elif nodeName_ == 'rated-weight' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'rated_weight')
            fval_ = self.gds_validate_decimal(fval_, node, 'rated_weight')
            self.rated_weight = fval_
            self.rated_weight_nsprefix_ = child_.prefix
            # validate type rated-weightType
            self.validate_rated_weightType(self.rated_weight)
# end class ShipmentPriceType


class ServiceStandardType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, am_delivery=None, guaranteed_delivery=None, expected_transmit_time=None, expected_delivery_date=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.am_delivery = am_delivery
        self.am_delivery_nsprefix_ = None
        self.guaranteed_delivery = guaranteed_delivery
        self.guaranteed_delivery_nsprefix_ = None
        self.expected_transmit_time = expected_transmit_time
        self.validate_expected_transmit_timeType(self.expected_transmit_time)
        self.expected_transmit_time_nsprefix_ = None
        if isinstance(expected_delivery_date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(expected_delivery_date, '%Y-%m-%d').date()
        else:
            initvalue_ = expected_delivery_date
        self.expected_delivery_date = initvalue_
        self.expected_delivery_date_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceStandardType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceStandardType.subclass:
            return ServiceStandardType.subclass(*args_, **kwargs_)
        else:
            return ServiceStandardType(*args_, **kwargs_)
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
    def get_expected_transmit_time(self):
        return self.expected_transmit_time
    def set_expected_transmit_time(self, expected_transmit_time):
        self.expected_transmit_time = expected_transmit_time
    def get_expected_delivery_date(self):
        return self.expected_delivery_date
    def set_expected_delivery_date(self, expected_delivery_date):
        self.expected_delivery_date = expected_delivery_date
    def validate_expected_transmit_timeType(self, value):
        result = True
        # Validate type expected-transmit-timeType, a restriction on xsd:integer.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on expected-transmit-timeType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 99:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on expected-transmit-timeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.am_delivery is not None or
            self.guaranteed_delivery is not None or
            self.expected_transmit_time is not None or
            self.expected_delivery_date is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ServiceStandardType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceStandardType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceStandardType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceStandardType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceStandardType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceStandardType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ServiceStandardType', fromsubclass_=False, pretty_print=True):
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
        if self.expected_transmit_time is not None:
            namespaceprefix_ = self.expected_transmit_time_nsprefix_ + ':' if (UseCapturedNS_ and self.expected_transmit_time_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexpected-transmit-time>%s</%sexpected-transmit-time>%s' % (namespaceprefix_ , self.gds_format_integer(self.expected_transmit_time, input_name='expected-transmit-time'), namespaceprefix_ , eol_))
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
        elif nodeName_ == 'expected-transmit-time' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'expected_transmit_time')
            ival_ = self.gds_validate_integer(ival_, node, 'expected_transmit_time')
            self.expected_transmit_time = ival_
            self.expected_transmit_time_nsprefix_ = child_.prefix
            # validate type expected-transmit-timeType
            self.validate_expected_transmit_timeType(self.expected_transmit_time)
        elif nodeName_ == 'expected-delivery-date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.expected_delivery_date = dval_
            self.expected_delivery_date_nsprefix_ = child_.prefix
# end class ServiceStandardType


class PricedOptionsType(GeneratedsSuper):
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
                CurrentSubclassModule_, PricedOptionsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PricedOptionsType.subclass:
            return PricedOptionsType.subclass(*args_, **kwargs_)
        else:
            return PricedOptionsType(*args_, **kwargs_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PricedOptionsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PricedOptionsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PricedOptionsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PricedOptionsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PricedOptionsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PricedOptionsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PricedOptionsType', fromsubclass_=False, pretty_print=True):
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
            obj_ = PricedOptionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.priced_option.append(obj_)
            obj_.original_tagname_ = 'priced-option'
# end class PricedOptionsType


class PricedOptionType(GeneratedsSuper):
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
        self.option_code_nsprefix_ = None
        self.option_price = option_price
        self.option_price_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PricedOptionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PricedOptionType.subclass:
            return PricedOptionType.subclass(*args_, **kwargs_)
        else:
            return PricedOptionType(*args_, **kwargs_)
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
    def _hasContent(self):
        if (
            self.option_code is not None or
            self.option_price is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PricedOptionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PricedOptionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PricedOptionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PricedOptionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PricedOptionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PricedOptionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PricedOptionType', fromsubclass_=False, pretty_print=True):
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
        elif nodeName_ == 'option-price':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'option_price')
            value_ = self.gds_validate_string(value_, node, 'option_price')
            self.option_price = value_
            self.option_price_nsprefix_ = child_.prefix
# end class PricedOptionType


class AdjustmentsType(GeneratedsSuper):
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
                CurrentSubclassModule_, AdjustmentsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AdjustmentsType.subclass:
            return AdjustmentsType.subclass(*args_, **kwargs_)
        else:
            return AdjustmentsType(*args_, **kwargs_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AdjustmentsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AdjustmentsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AdjustmentsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AdjustmentsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AdjustmentsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AdjustmentsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AdjustmentsType', fromsubclass_=False, pretty_print=True):
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
            obj_ = AdjustmentType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.adjustment.append(obj_)
            obj_.original_tagname_ = 'adjustment'
# end class AdjustmentsType


class AdjustmentType(GeneratedsSuper):
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
        self.adjustment_code_nsprefix_ = None
        self.adjustment_amount = adjustment_amount
        self.adjustment_amount_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AdjustmentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AdjustmentType.subclass:
            return AdjustmentType.subclass(*args_, **kwargs_)
        else:
            return AdjustmentType(*args_, **kwargs_)
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
    def _hasContent(self):
        if (
            self.adjustment_code is not None or
            self.adjustment_amount is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AdjustmentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AdjustmentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AdjustmentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AdjustmentType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AdjustmentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AdjustmentType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AdjustmentType', fromsubclass_=False, pretty_print=True):
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
        elif nodeName_ == 'adjustment-amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'adjustment_amount')
            value_ = self.gds_validate_string(value_, node, 'adjustment_amount')
            self.adjustment_amount = value_
            self.adjustment_amount_nsprefix_ = child_.prefix
# end class AdjustmentType


class ShipmentsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, link=None, shipment_info=None, gds_collector_=None, **kwargs_):
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
        if shipment_info is None:
            self.shipment_info = []
        else:
            self.shipment_info = shipment_info
        self.shipment_info_nsprefix_ = None
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
    def get_shipment_info(self):
        return self.shipment_info
    def set_shipment_info(self, shipment_info):
        self.shipment_info = shipment_info
    def add_shipment_info(self, value):
        self.shipment_info.append(value)
    def insert_shipment_info_at(self, index, value):
        self.shipment_info.insert(index, value)
    def replace_shipment_info_at(self, index, value):
        self.shipment_info[index] = value
    def _hasContent(self):
        if (
            self.link or
            self.shipment_info
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
        for shipment_info_ in self.shipment_info:
            namespaceprefix_ = self.shipment_info_nsprefix_ + ':' if (UseCapturedNS_ and self.shipment_info_nsprefix_) else ''
            shipment_info_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='shipment-info', pretty_print=pretty_print)
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
        elif nodeName_ == 'shipment-info':
            obj_ = ShipmentInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.shipment_info.append(obj_)
            obj_.original_tagname_ = 'shipment-info'
# end class ShipmentsType


class ShipmentInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, customer_request_id=None, shipment_id=None, shipment_status=None, tracking_pin=None, return_tracking_pin=None, po_number=None, shipment_price=None, shipment_receipt=None, links=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customer_request_id = customer_request_id
        self.validate_CustomerRequestIdType(self.customer_request_id)
        self.customer_request_id_nsprefix_ = None
        self.shipment_id = shipment_id
        self.validate_ShipmentIDType(self.shipment_id)
        self.shipment_id_nsprefix_ = None
        self.shipment_status = shipment_status
        self.validate_ShipmentStatusType(self.shipment_status)
        self.shipment_status_nsprefix_ = None
        self.tracking_pin = tracking_pin
        self.validate_TrackingPINType(self.tracking_pin)
        self.tracking_pin_nsprefix_ = None
        self.return_tracking_pin = return_tracking_pin
        self.validate_TrackingPINType(self.return_tracking_pin)
        self.return_tracking_pin_nsprefix_ = None
        self.po_number = po_number
        self.po_number_nsprefix_ = None
        self.shipment_price = shipment_price
        self.shipment_price_nsprefix_ = None
        self.shipment_receipt = shipment_receipt
        self.shipment_receipt_nsprefix_ = None
        self.links = links
        self.links_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentInfoType.subclass:
            return ShipmentInfoType.subclass(*args_, **kwargs_)
        else:
            return ShipmentInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_customer_request_id(self):
        return self.customer_request_id
    def set_customer_request_id(self, customer_request_id):
        self.customer_request_id = customer_request_id
    def get_shipment_id(self):
        return self.shipment_id
    def set_shipment_id(self, shipment_id):
        self.shipment_id = shipment_id
    def get_shipment_status(self):
        return self.shipment_status
    def set_shipment_status(self, shipment_status):
        self.shipment_status = shipment_status
    def get_tracking_pin(self):
        return self.tracking_pin
    def set_tracking_pin(self, tracking_pin):
        self.tracking_pin = tracking_pin
    def get_return_tracking_pin(self):
        return self.return_tracking_pin
    def set_return_tracking_pin(self, return_tracking_pin):
        self.return_tracking_pin = return_tracking_pin
    def get_po_number(self):
        return self.po_number
    def set_po_number(self, po_number):
        self.po_number = po_number
    def get_shipment_price(self):
        return self.shipment_price
    def set_shipment_price(self, shipment_price):
        self.shipment_price = shipment_price
    def get_shipment_receipt(self):
        return self.shipment_receipt
    def set_shipment_receipt(self, shipment_receipt):
        self.shipment_receipt = shipment_receipt
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
    def validate_ShipmentStatusType(self, value):
        result = True
        # Validate type ShipmentStatusType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ShipmentStatusType' % {"value": value, "lineno": lineno} )
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
            self.customer_request_id is not None or
            self.shipment_id is not None or
            self.shipment_status is not None or
            self.tracking_pin is not None or
            self.return_tracking_pin is not None or
            self.po_number is not None or
            self.shipment_price is not None or
            self.shipment_receipt is not None or
            self.links is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.customer_request_id is not None:
            namespaceprefix_ = self.customer_request_id_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_request_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-request-id>%s</%scustomer-request-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_request_id), input_name='customer-request-id')), namespaceprefix_ , eol_))
        if self.shipment_id is not None:
            namespaceprefix_ = self.shipment_id_nsprefix_ + ':' if (UseCapturedNS_ and self.shipment_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshipment-id>%s</%sshipment-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.shipment_id), input_name='shipment-id')), namespaceprefix_ , eol_))
        if self.shipment_status is not None:
            namespaceprefix_ = self.shipment_status_nsprefix_ + ':' if (UseCapturedNS_ and self.shipment_status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshipment-status>%s</%sshipment-status>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.shipment_status), input_name='shipment-status')), namespaceprefix_ , eol_))
        if self.tracking_pin is not None:
            namespaceprefix_ = self.tracking_pin_nsprefix_ + ':' if (UseCapturedNS_ and self.tracking_pin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stracking-pin>%s</%stracking-pin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tracking_pin), input_name='tracking-pin')), namespaceprefix_ , eol_))
        if self.return_tracking_pin is not None:
            namespaceprefix_ = self.return_tracking_pin_nsprefix_ + ':' if (UseCapturedNS_ and self.return_tracking_pin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreturn-tracking-pin>%s</%sreturn-tracking-pin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.return_tracking_pin), input_name='return-tracking-pin')), namespaceprefix_ , eol_))
        if self.po_number is not None:
            namespaceprefix_ = self.po_number_nsprefix_ + ':' if (UseCapturedNS_ and self.po_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spo-number>%s</%spo-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.po_number), input_name='po-number')), namespaceprefix_ , eol_))
        if self.shipment_price is not None:
            namespaceprefix_ = self.shipment_price_nsprefix_ + ':' if (UseCapturedNS_ and self.shipment_price_nsprefix_) else ''
            self.shipment_price.export(outfile, level, namespaceprefix_, namespacedef_='', name_='shipment-price', pretty_print=pretty_print)
        if self.shipment_receipt is not None:
            namespaceprefix_ = self.shipment_receipt_nsprefix_ + ':' if (UseCapturedNS_ and self.shipment_receipt_nsprefix_) else ''
            self.shipment_receipt.export(outfile, level, namespaceprefix_, namespacedef_='', name_='shipment-receipt', pretty_print=pretty_print)
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
        elif nodeName_ == 'shipment-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shipment_id')
            value_ = self.gds_validate_string(value_, node, 'shipment_id')
            self.shipment_id = value_
            self.shipment_id_nsprefix_ = child_.prefix
            # validate type ShipmentIDType
            self.validate_ShipmentIDType(self.shipment_id)
        elif nodeName_ == 'shipment-status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shipment_status')
            value_ = self.gds_validate_string(value_, node, 'shipment_status')
            self.shipment_status = value_
            self.shipment_status_nsprefix_ = child_.prefix
            # validate type ShipmentStatusType
            self.validate_ShipmentStatusType(self.shipment_status)
        elif nodeName_ == 'tracking-pin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tracking_pin')
            value_ = self.gds_validate_string(value_, node, 'tracking_pin')
            self.tracking_pin = value_
            self.tracking_pin_nsprefix_ = child_.prefix
            # validate type TrackingPINType
            self.validate_TrackingPINType(self.tracking_pin)
        elif nodeName_ == 'return-tracking-pin':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'return_tracking_pin')
            value_ = self.gds_validate_string(value_, node, 'return_tracking_pin')
            self.return_tracking_pin = value_
            self.return_tracking_pin_nsprefix_ = child_.prefix
            # validate type TrackingPINType
            self.validate_TrackingPINType(self.return_tracking_pin)
        elif nodeName_ == 'po-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'po_number')
            value_ = self.gds_validate_string(value_, node, 'po_number')
            self.po_number = value_
            self.po_number_nsprefix_ = child_.prefix
        elif nodeName_ == 'shipment-price':
            obj_ = ShipmentPriceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.shipment_price = obj_
            obj_.original_tagname_ = 'shipment-price'
        elif nodeName_ == 'shipment-receipt':
            obj_ = ShipmentReceiptType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.shipment_receipt = obj_
            obj_.original_tagname_ = 'shipment-receipt'
        elif nodeName_ == 'links':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'links')
            value_ = self.gds_validate_string(value_, node, 'links')
            self.links = value_
            self.links_nsprefix_ = child_.prefix
# end class ShipmentInfoType


class groupIdOrTransmitShipment(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, groupIdOrTransmitShipment)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if groupIdOrTransmitShipment.subclass:
            return groupIdOrTransmitShipment.subclass(*args_, **kwargs_)
        else:
            return groupIdOrTransmitShipment(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='groupIdOrTransmitShipment', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('groupIdOrTransmitShipment')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'groupIdOrTransmitShipment':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='groupIdOrTransmitShipment')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='groupIdOrTransmitShipment', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='groupIdOrTransmitShipment'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='groupIdOrTransmitShipment', fromsubclass_=False, pretty_print=True):
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class groupIdOrTransmitShipment


class ShipmentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, customer_request_id=None, groupIdOrTransmitShipment=None, quickship_label_requested=None, cpc_pickup_indicator=None, requested_shipping_point=None, shipping_point_id=None, expected_mailing_date=None, provide_pricing_info=None, provide_receipt_info=None, delivery_spec=None, return_spec=None, pre_authorized_payment=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customer_request_id = customer_request_id
        self.validate_CustomerRequestIdType(self.customer_request_id)
        self.customer_request_id_nsprefix_ = None
        self.groupIdOrTransmitShipment = groupIdOrTransmitShipment
        self.groupIdOrTransmitShipment_nsprefix_ = None
        self.quickship_label_requested = quickship_label_requested
        self.quickship_label_requested_nsprefix_ = None
        self.cpc_pickup_indicator = cpc_pickup_indicator
        self.cpc_pickup_indicator_nsprefix_ = None
        self.requested_shipping_point = requested_shipping_point
        self.requested_shipping_point_nsprefix_ = None
        self.shipping_point_id = shipping_point_id
        self.shipping_point_id_nsprefix_ = None
        if isinstance(expected_mailing_date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(expected_mailing_date, '%Y-%m-%d').date()
        else:
            initvalue_ = expected_mailing_date
        self.expected_mailing_date = initvalue_
        self.expected_mailing_date_nsprefix_ = None
        self.provide_pricing_info = provide_pricing_info
        self.provide_pricing_info_nsprefix_ = None
        self.provide_receipt_info = provide_receipt_info
        self.provide_receipt_info_nsprefix_ = None
        self.delivery_spec = delivery_spec
        self.delivery_spec_nsprefix_ = None
        self.return_spec = return_spec
        self.return_spec_nsprefix_ = None
        self.pre_authorized_payment = pre_authorized_payment
        self.pre_authorized_payment_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentType.subclass:
            return ShipmentType.subclass(*args_, **kwargs_)
        else:
            return ShipmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_customer_request_id(self):
        return self.customer_request_id
    def set_customer_request_id(self, customer_request_id):
        self.customer_request_id = customer_request_id
    def get_groupIdOrTransmitShipment(self):
        return self.groupIdOrTransmitShipment
    def set_groupIdOrTransmitShipment(self, groupIdOrTransmitShipment):
        self.groupIdOrTransmitShipment = groupIdOrTransmitShipment
    def get_quickship_label_requested(self):
        return self.quickship_label_requested
    def set_quickship_label_requested(self, quickship_label_requested):
        self.quickship_label_requested = quickship_label_requested
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
    def get_expected_mailing_date(self):
        return self.expected_mailing_date
    def set_expected_mailing_date(self, expected_mailing_date):
        self.expected_mailing_date = expected_mailing_date
    def get_provide_pricing_info(self):
        return self.provide_pricing_info
    def set_provide_pricing_info(self, provide_pricing_info):
        self.provide_pricing_info = provide_pricing_info
    def get_provide_receipt_info(self):
        return self.provide_receipt_info
    def set_provide_receipt_info(self, provide_receipt_info):
        self.provide_receipt_info = provide_receipt_info
    def get_delivery_spec(self):
        return self.delivery_spec
    def set_delivery_spec(self, delivery_spec):
        self.delivery_spec = delivery_spec
    def get_return_spec(self):
        return self.return_spec
    def set_return_spec(self, return_spec):
        self.return_spec = return_spec
    def get_pre_authorized_payment(self):
        return self.pre_authorized_payment
    def set_pre_authorized_payment(self, pre_authorized_payment):
        self.pre_authorized_payment = pre_authorized_payment
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
            self.groupIdOrTransmitShipment is not None or
            self.quickship_label_requested is not None or
            self.cpc_pickup_indicator is not None or
            self.requested_shipping_point is not None or
            self.shipping_point_id is not None or
            self.expected_mailing_date is not None or
            self.provide_pricing_info is not None or
            self.provide_receipt_info is not None or
            self.delivery_spec is not None or
            self.return_spec is not None or
            self.pre_authorized_payment is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.customer_request_id is not None:
            namespaceprefix_ = self.customer_request_id_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_request_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-request-id>%s</%scustomer-request-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_request_id), input_name='customer-request-id')), namespaceprefix_ , eol_))
        if self.groupIdOrTransmitShipment is not None:
            self.groupIdOrTransmitShipment.export(outfile, level, namespaceprefix_, namespacedef_='', pretty_print=pretty_print)
        if self.quickship_label_requested is not None:
            namespaceprefix_ = self.quickship_label_requested_nsprefix_ + ':' if (UseCapturedNS_ and self.quickship_label_requested_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%squickship-label-requested>%s</%squickship-label-requested>%s' % (namespaceprefix_ , self.gds_format_boolean(self.quickship_label_requested, input_name='quickship-label-requested'), namespaceprefix_ , eol_))
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
        if self.expected_mailing_date is not None:
            namespaceprefix_ = self.expected_mailing_date_nsprefix_ + ':' if (UseCapturedNS_ and self.expected_mailing_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexpected-mailing-date>%s</%sexpected-mailing-date>%s' % (namespaceprefix_ , self.gds_format_date(self.expected_mailing_date, input_name='expected-mailing-date'), namespaceprefix_ , eol_))
        if self.provide_pricing_info is not None:
            namespaceprefix_ = self.provide_pricing_info_nsprefix_ + ':' if (UseCapturedNS_ and self.provide_pricing_info_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprovide-pricing-info>%s</%sprovide-pricing-info>%s' % (namespaceprefix_ , self.gds_format_boolean(self.provide_pricing_info, input_name='provide-pricing-info'), namespaceprefix_ , eol_))
        if self.provide_receipt_info is not None:
            namespaceprefix_ = self.provide_receipt_info_nsprefix_ + ':' if (UseCapturedNS_ and self.provide_receipt_info_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprovide-receipt-info>%s</%sprovide-receipt-info>%s' % (namespaceprefix_ , self.gds_format_boolean(self.provide_receipt_info, input_name='provide-receipt-info'), namespaceprefix_ , eol_))
        if self.delivery_spec is not None:
            namespaceprefix_ = self.delivery_spec_nsprefix_ + ':' if (UseCapturedNS_ and self.delivery_spec_nsprefix_) else ''
            self.delivery_spec.export(outfile, level, namespaceprefix_, namespacedef_='', name_='delivery-spec', pretty_print=pretty_print)
        if self.return_spec is not None:
            namespaceprefix_ = self.return_spec_nsprefix_ + ':' if (UseCapturedNS_ and self.return_spec_nsprefix_) else ''
            self.return_spec.export(outfile, level, namespaceprefix_, namespacedef_='', name_='return-spec', pretty_print=pretty_print)
        if self.pre_authorized_payment is not None:
            namespaceprefix_ = self.pre_authorized_payment_nsprefix_ + ':' if (UseCapturedNS_ and self.pre_authorized_payment_nsprefix_) else ''
            self.pre_authorized_payment.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pre-authorized-payment', pretty_print=pretty_print)
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
        elif nodeName_ == 'groupIdOrTransmitShipment':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_, gds_collector_=gds_collector_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <groupIdOrTransmitShipment> element')
            self.groupIdOrTransmitShipment = obj_
            obj_.original_tagname_ = 'groupIdOrTransmitShipment'
        elif nodeName_ == 'quickship-label-requested':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'quickship_label_requested')
            ival_ = self.gds_validate_boolean(ival_, node, 'quickship_label_requested')
            self.quickship_label_requested = ival_
            self.quickship_label_requested_nsprefix_ = child_.prefix
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
        elif nodeName_ == 'expected-mailing-date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.expected_mailing_date = dval_
            self.expected_mailing_date_nsprefix_ = child_.prefix
        elif nodeName_ == 'provide-pricing-info':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'provide_pricing_info')
            ival_ = self.gds_validate_boolean(ival_, node, 'provide_pricing_info')
            self.provide_pricing_info = ival_
            self.provide_pricing_info_nsprefix_ = child_.prefix
        elif nodeName_ == 'provide-receipt-info':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'provide_receipt_info')
            ival_ = self.gds_validate_boolean(ival_, node, 'provide_receipt_info')
            self.provide_receipt_info = ival_
            self.provide_receipt_info_nsprefix_ = child_.prefix
        elif nodeName_ == 'delivery-spec':
            obj_ = DeliverySpecType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.delivery_spec = obj_
            obj_.original_tagname_ = 'delivery-spec'
        elif nodeName_ == 'return-spec':
            obj_ = ReturnSpecType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.return_spec = obj_
            obj_.original_tagname_ = 'return-spec'
        elif nodeName_ == 'pre-authorized-payment':
            obj_ = PreAuthorizedPaymentType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pre_authorized_payment = obj_
            obj_.original_tagname_ = 'pre-authorized-payment'
# end class ShipmentType


class DeliverySpecType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service_code=None, sender=None, destination=None, options=None, parcel_characteristics=None, notification=None, print_preferences=None, preferences=None, references=None, customs=None, settlement_info=None, gds_collector_=None, **kwargs_):
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
        self.print_preferences = print_preferences
        self.print_preferences_nsprefix_ = None
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
    def get_print_preferences(self):
        return self.print_preferences
    def set_print_preferences(self, print_preferences):
        self.print_preferences = print_preferences
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
            self.print_preferences is not None or
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
        if self.print_preferences is not None:
            namespaceprefix_ = self.print_preferences_nsprefix_ + ':' if (UseCapturedNS_ and self.print_preferences_nsprefix_) else ''
            self.print_preferences.export(outfile, level, namespaceprefix_, namespacedef_='', name_='print-preferences', pretty_print=pretty_print)
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
        elif nodeName_ == 'print-preferences':
            obj_ = PrintPreferencesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.print_preferences = obj_
            obj_.original_tagname_ = 'print-preferences'
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
        self.validate_currencyType(self.currency)
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
    def validate_currencyType(self, value):
        result = True
        # Validate type currencyType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on currencyType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on currencyType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
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
            # validate type currencyType
            self.validate_currencyType(self.currency)
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
            obj_ = AddressDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address_details = obj_
            obj_.original_tagname_ = 'address-details'
# end class SenderType


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
        self.validate_additional_address_infoType(self.additional_address_info)
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
# end class DestinationType


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
        self.validate_additional_address_infoType1(self.additional_address_info)
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
    def validate_additional_address_infoType1(self, value):
        result = True
        # Validate type additional-address-infoType1, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on additional-address-infoType1' % {"value": value, "lineno": lineno} )
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
            # validate type additional-address-infoType1
            self.validate_additional_address_infoType1(self.additional_address_info)
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


class ReturnSpecType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service_code=None, return_recipient=None, return_notification=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.service_code = service_code
        self.service_code_nsprefix_ = None
        self.return_recipient = return_recipient
        self.return_recipient_nsprefix_ = None
        self.return_notification = return_notification
        self.validate_EmailType(self.return_notification)
        self.return_notification_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReturnSpecType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReturnSpecType.subclass:
            return ReturnSpecType.subclass(*args_, **kwargs_)
        else:
            return ReturnSpecType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_service_code(self):
        return self.service_code
    def set_service_code(self, service_code):
        self.service_code = service_code
    def get_return_recipient(self):
        return self.return_recipient
    def set_return_recipient(self, return_recipient):
        self.return_recipient = return_recipient
    def get_return_notification(self):
        return self.return_notification
    def set_return_notification(self, return_notification):
        self.return_notification = return_notification
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
            self.service_code is not None or
            self.return_recipient is not None or
            self.return_notification is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ReturnSpecType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReturnSpecType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReturnSpecType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReturnSpecType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReturnSpecType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ReturnSpecType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ReturnSpecType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.service_code is not None:
            namespaceprefix_ = self.service_code_nsprefix_ + ':' if (UseCapturedNS_ and self.service_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-code>%s</%sservice-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.service_code), input_name='service-code')), namespaceprefix_ , eol_))
        if self.return_recipient is not None:
            namespaceprefix_ = self.return_recipient_nsprefix_ + ':' if (UseCapturedNS_ and self.return_recipient_nsprefix_) else ''
            self.return_recipient.export(outfile, level, namespaceprefix_, namespacedef_='', name_='return-recipient', pretty_print=pretty_print)
        if self.return_notification is not None:
            namespaceprefix_ = self.return_notification_nsprefix_ + ':' if (UseCapturedNS_ and self.return_notification_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreturn-notification>%s</%sreturn-notification>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.return_notification), input_name='return-notification')), namespaceprefix_ , eol_))
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
        elif nodeName_ == 'return-recipient':
            obj_ = ReturnRecipientType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.return_recipient = obj_
            obj_.original_tagname_ = 'return-recipient'
        elif nodeName_ == 'return-notification':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'return_notification')
            value_ = self.gds_validate_string(value_, node, 'return_notification')
            self.return_notification = value_
            self.return_notification_nsprefix_ = child_.prefix
            # validate type EmailType
            self.validate_EmailType(self.return_notification)
# end class ReturnSpecType


class ReturnRecipientType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, company=None, address_details=None, gds_collector_=None, **kwargs_):
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
        self.address_details = address_details
        self.address_details_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReturnRecipientType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReturnRecipientType.subclass:
            return ReturnRecipientType.subclass(*args_, **kwargs_)
        else:
            return ReturnRecipientType(*args_, **kwargs_)
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
            self.address_details is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ReturnRecipientType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReturnRecipientType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReturnRecipientType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReturnRecipientType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReturnRecipientType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ReturnRecipientType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ReturnRecipientType', fromsubclass_=False, pretty_print=True):
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
        elif nodeName_ == 'address-details':
            obj_ = DomesticAddressDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address_details = obj_
            obj_.original_tagname_ = 'address-details'
# end class ReturnRecipientType


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
        self.validate_address_line_1Type2(self.address_line_1)
        self.address_line_1_nsprefix_ = None
        self.address_line_2 = address_line_2
        self.validate_address_line_2Type3(self.address_line_2)
        self.address_line_2_nsprefix_ = None
        self.city = city
        self.validate_cityType4(self.city)
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
    def validate_address_line_1Type2(self, value):
        result = True
        # Validate type address-line-1Type2, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on address-line-1Type2' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on address-line-1Type2' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_address_line_2Type3(self, value):
        result = True
        # Validate type address-line-2Type3, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on address-line-2Type3' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_cityType4(self, value):
        result = True
        # Validate type cityType4, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on cityType4' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on cityType4' % {"value" : value, "lineno": lineno} )
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
            # validate type address-line-1Type2
            self.validate_address_line_1Type2(self.address_line_1)
        elif nodeName_ == 'address-line-2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'address_line_2')
            value_ = self.gds_validate_string(value_, node, 'address_line_2')
            self.address_line_2 = value_
            self.address_line_2_nsprefix_ = child_.prefix
            # validate type address-line-2Type3
            self.validate_address_line_2Type3(self.address_line_2)
        elif nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type cityType4
            self.validate_cityType4(self.city)
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
        self.validate_address_line_1Type5(self.address_line_1)
        self.address_line_1_nsprefix_ = None
        self.address_line_2 = address_line_2
        self.validate_address_line_2Type6(self.address_line_2)
        self.address_line_2_nsprefix_ = None
        self.city = city
        self.validate_cityType7(self.city)
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
    def validate_address_line_1Type5(self, value):
        result = True
        # Validate type address-line-1Type5, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on address-line-1Type5' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on address-line-1Type5' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_address_line_2Type6(self, value):
        result = True
        # Validate type address-line-2Type6, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on address-line-2Type6' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_cityType7(self, value):
        result = True
        # Validate type cityType7, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on cityType7' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on cityType7' % {"value" : value, "lineno": lineno} )
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
            # validate type address-line-1Type5
            self.validate_address_line_1Type5(self.address_line_1)
        elif nodeName_ == 'address-line-2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'address_line_2')
            value_ = self.gds_validate_string(value_, node, 'address_line_2')
            self.address_line_2 = value_
            self.address_line_2_nsprefix_ = child_.prefix
            # validate type address-line-2Type6
            self.validate_address_line_2Type6(self.address_line_2)
        elif nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type cityType7
            self.validate_cityType7(self.city)
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
        self.validate_option_codeType(self.option_code)
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
            # validate type option-codeType
            self.validate_option_codeType(self.option_code)
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
            self.unpackaged is not None or
            self.mailing_tube is not None or
            self.oversized is not None
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


class PrintPreferencesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, output_format=None, encoding=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.output_format = output_format
        self.validate_output_formatType(self.output_format)
        self.output_format_nsprefix_ = None
        self.encoding = encoding
        self.validate_encodingType(self.encoding)
        self.encoding_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PrintPreferencesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PrintPreferencesType.subclass:
            return PrintPreferencesType.subclass(*args_, **kwargs_)
        else:
            return PrintPreferencesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_output_format(self):
        return self.output_format
    def set_output_format(self, output_format):
        self.output_format = output_format
    def get_encoding(self):
        return self.encoding
    def set_encoding(self, encoding):
        self.encoding = encoding
    def validate_output_formatType(self, value):
        result = True
        # Validate type output-formatType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['8.5x11', '4x6']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on output-formatType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_encodingType(self, value):
        result = True
        # Validate type encodingType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['PDF', 'ZPL']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on encodingType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.output_format is not None or
            self.encoding is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PrintPreferencesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PrintPreferencesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PrintPreferencesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PrintPreferencesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PrintPreferencesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PrintPreferencesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PrintPreferencesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.output_format is not None:
            namespaceprefix_ = self.output_format_nsprefix_ + ':' if (UseCapturedNS_ and self.output_format_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soutput-format>%s</%soutput-format>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.output_format), input_name='output-format')), namespaceprefix_ , eol_))
        if self.encoding is not None:
            namespaceprefix_ = self.encoding_nsprefix_ + ':' if (UseCapturedNS_ and self.encoding_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sencoding>%s</%sencoding>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.encoding), input_name='encoding')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'output-format':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'output_format')
            value_ = self.gds_validate_string(value_, node, 'output_format')
            self.output_format = value_
            self.output_format_nsprefix_ = child_.prefix
            # validate type output-formatType
            self.validate_output_formatType(self.output_format)
        elif nodeName_ == 'encoding':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'encoding')
            value_ = self.gds_validate_string(value_, node, 'encoding')
            self.encoding = value_
            self.encoding_nsprefix_ = child_.prefix
            # validate type encodingType
            self.validate_encodingType(self.encoding)
# end class PrintPreferencesType


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
    def __init__(self, paid_by_customer=None, contract_id=None, cif_shipment=None, intended_method_of_payment=None, promo_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.paid_by_customer = paid_by_customer
        self.paid_by_customer_nsprefix_ = None
        self.contract_id = contract_id
        self.contract_id_nsprefix_ = None
        self.cif_shipment = cif_shipment
        self.cif_shipment_nsprefix_ = None
        self.intended_method_of_payment = intended_method_of_payment
        self.intended_method_of_payment_nsprefix_ = None
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
    def get_paid_by_customer(self):
        return self.paid_by_customer
    def set_paid_by_customer(self, paid_by_customer):
        self.paid_by_customer = paid_by_customer
    def get_contract_id(self):
        return self.contract_id
    def set_contract_id(self, contract_id):
        self.contract_id = contract_id
    def get_cif_shipment(self):
        return self.cif_shipment
    def set_cif_shipment(self, cif_shipment):
        self.cif_shipment = cif_shipment
    def get_intended_method_of_payment(self):
        return self.intended_method_of_payment
    def set_intended_method_of_payment(self, intended_method_of_payment):
        self.intended_method_of_payment = intended_method_of_payment
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
            self.paid_by_customer is not None or
            self.contract_id is not None or
            self.cif_shipment is not None or
            self.intended_method_of_payment is not None or
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
        if self.paid_by_customer is not None:
            namespaceprefix_ = self.paid_by_customer_nsprefix_ + ':' if (UseCapturedNS_ and self.paid_by_customer_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spaid-by-customer>%s</%spaid-by-customer>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.paid_by_customer), input_name='paid-by-customer')), namespaceprefix_ , eol_))
        if self.contract_id is not None:
            namespaceprefix_ = self.contract_id_nsprefix_ + ':' if (UseCapturedNS_ and self.contract_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontract-id>%s</%scontract-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contract_id), input_name='contract-id')), namespaceprefix_ , eol_))
        if self.cif_shipment is not None:
            namespaceprefix_ = self.cif_shipment_nsprefix_ + ':' if (UseCapturedNS_ and self.cif_shipment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scif-shipment>%s</%scif-shipment>%s' % (namespaceprefix_ , self.gds_format_boolean(self.cif_shipment, input_name='cif-shipment'), namespaceprefix_ , eol_))
        if self.intended_method_of_payment is not None:
            namespaceprefix_ = self.intended_method_of_payment_nsprefix_ + ':' if (UseCapturedNS_ and self.intended_method_of_payment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sintended-method-of-payment>%s</%sintended-method-of-payment>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.intended_method_of_payment), input_name='intended-method-of-payment')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'paid-by-customer':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'paid_by_customer')
            value_ = self.gds_validate_string(value_, node, 'paid_by_customer')
            self.paid_by_customer = value_
            self.paid_by_customer_nsprefix_ = child_.prefix
        elif nodeName_ == 'contract-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contract_id')
            value_ = self.gds_validate_string(value_, node, 'contract_id')
            self.contract_id = value_
            self.contract_id_nsprefix_ = child_.prefix
        elif nodeName_ == 'cif-shipment':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'cif_shipment')
            ival_ = self.gds_validate_boolean(ival_, node, 'cif_shipment')
            self.cif_shipment = ival_
            self.cif_shipment_nsprefix_ = child_.prefix
        elif nodeName_ == 'intended-method-of-payment':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'intended_method_of_payment')
            value_ = self.gds_validate_string(value_, node, 'intended_method_of_payment')
            self.intended_method_of_payment = value_
            self.intended_method_of_payment_nsprefix_ = child_.prefix
        elif nodeName_ == 'promo-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'promo_code')
            value_ = self.gds_validate_string(value_, node, 'promo_code')
            self.promo_code = value_
            self.promo_code_nsprefix_ = child_.prefix
            # validate type PromoCodeType
            self.validate_PromoCodeType(self.promo_code)
# end class SettlementInfoType


class PreAuthorizedPaymentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, account_number=None, auth_code=None, auth_timestamp=None, charge_amount=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.account_number = account_number
        self.validate_account_numberType(self.account_number)
        self.account_number_nsprefix_ = None
        self.auth_code = auth_code
        self.validate_auth_codeType(self.auth_code)
        self.auth_code_nsprefix_ = None
        if isinstance(auth_timestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(auth_timestamp, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = auth_timestamp
        self.auth_timestamp = initvalue_
        self.auth_timestamp_nsprefix_ = None
        self.charge_amount = charge_amount
        self.validate_charge_amountType(self.charge_amount)
        self.charge_amount_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PreAuthorizedPaymentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PreAuthorizedPaymentType.subclass:
            return PreAuthorizedPaymentType.subclass(*args_, **kwargs_)
        else:
            return PreAuthorizedPaymentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_account_number(self):
        return self.account_number
    def set_account_number(self, account_number):
        self.account_number = account_number
    def get_auth_code(self):
        return self.auth_code
    def set_auth_code(self, auth_code):
        self.auth_code = auth_code
    def get_auth_timestamp(self):
        return self.auth_timestamp
    def set_auth_timestamp(self, auth_timestamp):
        self.auth_timestamp = auth_timestamp
    def get_charge_amount(self):
        return self.charge_amount
    def set_charge_amount(self, charge_amount):
        self.charge_amount = charge_amount
    def validate_account_numberType(self, value):
        result = True
        # Validate type account-numberType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on account-numberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on account-numberType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_auth_codeType(self, value):
        result = True
        # Validate type auth-codeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on auth-codeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on auth-codeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_charge_amountType(self, value):
        result = True
        # Validate type charge-amountType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value > 9999999.99:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on charge-amountType' % {"value": value, "lineno": lineno} )
                result = False
            if value <= 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minExclusive restriction on charge-amountType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.account_number is not None or
            self.auth_code is not None or
            self.auth_timestamp is not None or
            self.charge_amount is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PreAuthorizedPaymentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PreAuthorizedPaymentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PreAuthorizedPaymentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PreAuthorizedPaymentType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PreAuthorizedPaymentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PreAuthorizedPaymentType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PreAuthorizedPaymentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.account_number is not None:
            namespaceprefix_ = self.account_number_nsprefix_ + ':' if (UseCapturedNS_ and self.account_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saccount-number>%s</%saccount-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.account_number), input_name='account-number')), namespaceprefix_ , eol_))
        if self.auth_code is not None:
            namespaceprefix_ = self.auth_code_nsprefix_ + ':' if (UseCapturedNS_ and self.auth_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauth-code>%s</%sauth-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.auth_code), input_name='auth-code')), namespaceprefix_ , eol_))
        if self.auth_timestamp is not None:
            namespaceprefix_ = self.auth_timestamp_nsprefix_ + ':' if (UseCapturedNS_ and self.auth_timestamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauth-timestamp>%s</%sauth-timestamp>%s' % (namespaceprefix_ , self.gds_format_datetime(self.auth_timestamp, input_name='auth-timestamp'), namespaceprefix_ , eol_))
        if self.charge_amount is not None:
            namespaceprefix_ = self.charge_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.charge_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scharge-amount>%s</%scharge-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.charge_amount, input_name='charge-amount'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'account-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'account_number')
            value_ = self.gds_validate_string(value_, node, 'account_number')
            self.account_number = value_
            self.account_number_nsprefix_ = child_.prefix
            # validate type account-numberType
            self.validate_account_numberType(self.account_number)
        elif nodeName_ == 'auth-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'auth_code')
            value_ = self.gds_validate_string(value_, node, 'auth_code')
            self.auth_code = value_
            self.auth_code_nsprefix_ = child_.prefix
            # validate type auth-codeType
            self.validate_auth_codeType(self.auth_code)
        elif nodeName_ == 'auth-timestamp':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.auth_timestamp = dval_
            self.auth_timestamp_nsprefix_ = child_.prefix
        elif nodeName_ == 'charge-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'charge_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'charge_amount')
            self.charge_amount = fval_
            self.charge_amount_nsprefix_ = child_.prefix
            # validate type charge-amountType
            self.validate_charge_amountType(self.charge_amount)
# end class PreAuthorizedPaymentType


class ShipmentDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, customer_request_id=None, shipment_status=None, final_shipping_point=None, tracking_pin=None, po_number=None, shipping_point_id=None, cpc_pickup_indicator=None, shipment_detail=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customer_request_id = customer_request_id
        self.validate_CustomerRequestIdType(self.customer_request_id)
        self.customer_request_id_nsprefix_ = None
        self.shipment_status = shipment_status
        self.validate_ShipmentStatusType(self.shipment_status)
        self.shipment_status_nsprefix_ = None
        self.final_shipping_point = final_shipping_point
        self.final_shipping_point_nsprefix_ = None
        self.tracking_pin = tracking_pin
        self.validate_TrackingPINType(self.tracking_pin)
        self.tracking_pin_nsprefix_ = None
        self.po_number = po_number
        self.po_number_nsprefix_ = None
        self.shipping_point_id = shipping_point_id
        self.shipping_point_id_nsprefix_ = None
        self.cpc_pickup_indicator = cpc_pickup_indicator
        self.cpc_pickup_indicator_nsprefix_ = None
        self.shipment_detail = shipment_detail
        self.shipment_detail_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentDetailsType.subclass:
            return ShipmentDetailsType.subclass(*args_, **kwargs_)
        else:
            return ShipmentDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_customer_request_id(self):
        return self.customer_request_id
    def set_customer_request_id(self, customer_request_id):
        self.customer_request_id = customer_request_id
    def get_shipment_status(self):
        return self.shipment_status
    def set_shipment_status(self, shipment_status):
        self.shipment_status = shipment_status
    def get_final_shipping_point(self):
        return self.final_shipping_point
    def set_final_shipping_point(self, final_shipping_point):
        self.final_shipping_point = final_shipping_point
    def get_tracking_pin(self):
        return self.tracking_pin
    def set_tracking_pin(self, tracking_pin):
        self.tracking_pin = tracking_pin
    def get_po_number(self):
        return self.po_number
    def set_po_number(self, po_number):
        self.po_number = po_number
    def get_shipping_point_id(self):
        return self.shipping_point_id
    def set_shipping_point_id(self, shipping_point_id):
        self.shipping_point_id = shipping_point_id
    def get_cpc_pickup_indicator(self):
        return self.cpc_pickup_indicator
    def set_cpc_pickup_indicator(self, cpc_pickup_indicator):
        self.cpc_pickup_indicator = cpc_pickup_indicator
    def get_shipment_detail(self):
        return self.shipment_detail
    def set_shipment_detail(self, shipment_detail):
        self.shipment_detail = shipment_detail
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
    def validate_ShipmentStatusType(self, value):
        result = True
        # Validate type ShipmentStatusType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ShipmentStatusType' % {"value": value, "lineno": lineno} )
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
            self.customer_request_id is not None or
            self.shipment_status is not None or
            self.final_shipping_point is not None or
            self.tracking_pin is not None or
            self.po_number is not None or
            self.shipping_point_id is not None or
            self.cpc_pickup_indicator is not None or
            self.shipment_detail is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.customer_request_id is not None:
            namespaceprefix_ = self.customer_request_id_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_request_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-request-id>%s</%scustomer-request-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_request_id), input_name='customer-request-id')), namespaceprefix_ , eol_))
        if self.shipment_status is not None:
            namespaceprefix_ = self.shipment_status_nsprefix_ + ':' if (UseCapturedNS_ and self.shipment_status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshipment-status>%s</%sshipment-status>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.shipment_status), input_name='shipment-status')), namespaceprefix_ , eol_))
        if self.final_shipping_point is not None:
            namespaceprefix_ = self.final_shipping_point_nsprefix_ + ':' if (UseCapturedNS_ and self.final_shipping_point_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfinal-shipping-point>%s</%sfinal-shipping-point>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.final_shipping_point), input_name='final-shipping-point')), namespaceprefix_ , eol_))
        if self.tracking_pin is not None:
            namespaceprefix_ = self.tracking_pin_nsprefix_ + ':' if (UseCapturedNS_ and self.tracking_pin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stracking-pin>%s</%stracking-pin>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tracking_pin), input_name='tracking-pin')), namespaceprefix_ , eol_))
        if self.po_number is not None:
            namespaceprefix_ = self.po_number_nsprefix_ + ':' if (UseCapturedNS_ and self.po_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spo-number>%s</%spo-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.po_number), input_name='po-number')), namespaceprefix_ , eol_))
        if self.shipping_point_id is not None:
            namespaceprefix_ = self.shipping_point_id_nsprefix_ + ':' if (UseCapturedNS_ and self.shipping_point_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshipping-point-id>%s</%sshipping-point-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.shipping_point_id), input_name='shipping-point-id')), namespaceprefix_ , eol_))
        if self.cpc_pickup_indicator is not None:
            namespaceprefix_ = self.cpc_pickup_indicator_nsprefix_ + ':' if (UseCapturedNS_ and self.cpc_pickup_indicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scpc-pickup-indicator>%s</%scpc-pickup-indicator>%s' % (namespaceprefix_ , self.gds_format_boolean(self.cpc_pickup_indicator, input_name='cpc-pickup-indicator'), namespaceprefix_ , eol_))
        if self.shipment_detail is not None:
            namespaceprefix_ = self.shipment_detail_nsprefix_ + ':' if (UseCapturedNS_ and self.shipment_detail_nsprefix_) else ''
            self.shipment_detail.export(outfile, level, namespaceprefix_, namespacedef_='', name_='shipment-detail', pretty_print=pretty_print)
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
        elif nodeName_ == 'shipment-status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shipment_status')
            value_ = self.gds_validate_string(value_, node, 'shipment_status')
            self.shipment_status = value_
            self.shipment_status_nsprefix_ = child_.prefix
            # validate type ShipmentStatusType
            self.validate_ShipmentStatusType(self.shipment_status)
        elif nodeName_ == 'final-shipping-point':
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
        elif nodeName_ == 'po-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'po_number')
            value_ = self.gds_validate_string(value_, node, 'po_number')
            self.po_number = value_
            self.po_number_nsprefix_ = child_.prefix
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
        elif nodeName_ == 'shipment-detail':
            obj_ = shipment_detailType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.shipment_detail = obj_
            obj_.original_tagname_ = 'shipment-detail'
# end class ShipmentDetailsType


class ShipmentCCReceiptType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, cc_receipt_details=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.cc_receipt_details = cc_receipt_details
        self.cc_receipt_details_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentCCReceiptType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentCCReceiptType.subclass:
            return ShipmentCCReceiptType.subclass(*args_, **kwargs_)
        else:
            return ShipmentCCReceiptType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_cc_receipt_details(self):
        return self.cc_receipt_details
    def set_cc_receipt_details(self, cc_receipt_details):
        self.cc_receipt_details = cc_receipt_details
    def _hasContent(self):
        if (
            self.cc_receipt_details is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentCCReceiptType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentCCReceiptType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentCCReceiptType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentCCReceiptType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentCCReceiptType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentCCReceiptType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentCCReceiptType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cc_receipt_details is not None:
            namespaceprefix_ = self.cc_receipt_details_nsprefix_ + ':' if (UseCapturedNS_ and self.cc_receipt_details_nsprefix_) else ''
            self.cc_receipt_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='cc-receipt-details', pretty_print=pretty_print)
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
        if nodeName_ == 'cc-receipt-details':
            obj_ = cc_receipt_detailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.cc_receipt_details = obj_
            obj_.original_tagname_ = 'cc-receipt-details'
# end class ShipmentCCReceiptType


class ShipmentReceiptType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, cc_receipt_details=None, supplier_account_receipt_details=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.cc_receipt_details = cc_receipt_details
        self.cc_receipt_details_nsprefix_ = None
        self.supplier_account_receipt_details = supplier_account_receipt_details
        self.supplier_account_receipt_details_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentReceiptType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentReceiptType.subclass:
            return ShipmentReceiptType.subclass(*args_, **kwargs_)
        else:
            return ShipmentReceiptType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_cc_receipt_details(self):
        return self.cc_receipt_details
    def set_cc_receipt_details(self, cc_receipt_details):
        self.cc_receipt_details = cc_receipt_details
    def get_supplier_account_receipt_details(self):
        return self.supplier_account_receipt_details
    def set_supplier_account_receipt_details(self, supplier_account_receipt_details):
        self.supplier_account_receipt_details = supplier_account_receipt_details
    def _hasContent(self):
        if (
            self.cc_receipt_details is not None or
            self.supplier_account_receipt_details is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentReceiptType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentReceiptType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentReceiptType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentReceiptType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentReceiptType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentReceiptType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentReceiptType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cc_receipt_details is not None:
            namespaceprefix_ = self.cc_receipt_details_nsprefix_ + ':' if (UseCapturedNS_ and self.cc_receipt_details_nsprefix_) else ''
            self.cc_receipt_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='cc-receipt-details', pretty_print=pretty_print)
        if self.supplier_account_receipt_details is not None:
            namespaceprefix_ = self.supplier_account_receipt_details_nsprefix_ + ':' if (UseCapturedNS_ and self.supplier_account_receipt_details_nsprefix_) else ''
            self.supplier_account_receipt_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='supplier-account-receipt-details', pretty_print=pretty_print)
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
        if nodeName_ == 'cc-receipt-details':
            obj_ = cc_receipt_detailsType9.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.cc_receipt_details = obj_
            obj_.original_tagname_ = 'cc-receipt-details'
        elif nodeName_ == 'supplier-account-receipt-details':
            obj_ = supplier_account_receipt_detailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.supplier_account_receipt_details = obj_
            obj_.original_tagname_ = 'supplier-account-receipt-details'
# end class ShipmentReceiptType


class ShipmentRefundRequestType(GeneratedsSuper):
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
                CurrentSubclassModule_, ShipmentRefundRequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentRefundRequestType.subclass:
            return ShipmentRefundRequestType.subclass(*args_, **kwargs_)
        else:
            return ShipmentRefundRequestType(*args_, **kwargs_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentRefundRequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentRefundRequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentRefundRequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentRefundRequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentRefundRequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentRefundRequestType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentRefundRequestType', fromsubclass_=False, pretty_print=True):
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
# end class ShipmentRefundRequestType


class ShipmentRefundRequestInfoType(GeneratedsSuper):
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
                CurrentSubclassModule_, ShipmentRefundRequestInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentRefundRequestInfoType.subclass:
            return ShipmentRefundRequestInfoType.subclass(*args_, **kwargs_)
        else:
            return ShipmentRefundRequestInfoType(*args_, **kwargs_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentRefundRequestInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentRefundRequestInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentRefundRequestInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentRefundRequestInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentRefundRequestInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentRefundRequestInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentRefundRequestInfoType', fromsubclass_=False, pretty_print=True):
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
# end class ShipmentRefundRequestInfoType


class GroupIDType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GroupIDType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GroupIDType.subclass:
            return GroupIDType.subclass(*args_, **kwargs_)
        else:
            return GroupIDType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_GroupIDType_impl(self, value):
        result = True
        # Validate type GroupIDType_impl, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on GroupIDType_impl' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on GroupIDType_impl' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupIDType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GroupIDType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GroupIDType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GroupIDType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GroupIDType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GroupIDType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GroupIDType', fromsubclass_=False, pretty_print=True):
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
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class GroupIDType


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


class shipment_detailType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, groupIdOrTransmitShipment=None, quickship_label_requested=None, expected_mailing_date=None, delivery_spec=None, return_spec=None, refund_request_info=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.groupIdOrTransmitShipment = groupIdOrTransmitShipment
        self.groupIdOrTransmitShipment_nsprefix_ = None
        self.quickship_label_requested = quickship_label_requested
        self.quickship_label_requested_nsprefix_ = None
        if isinstance(expected_mailing_date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(expected_mailing_date, '%Y-%m-%d').date()
        else:
            initvalue_ = expected_mailing_date
        self.expected_mailing_date = initvalue_
        self.expected_mailing_date_nsprefix_ = None
        self.delivery_spec = delivery_spec
        self.delivery_spec_nsprefix_ = None
        self.return_spec = return_spec
        self.return_spec_nsprefix_ = None
        self.refund_request_info = refund_request_info
        self.refund_request_info_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, shipment_detailType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if shipment_detailType.subclass:
            return shipment_detailType.subclass(*args_, **kwargs_)
        else:
            return shipment_detailType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_groupIdOrTransmitShipment(self):
        return self.groupIdOrTransmitShipment
    def set_groupIdOrTransmitShipment(self, groupIdOrTransmitShipment):
        self.groupIdOrTransmitShipment = groupIdOrTransmitShipment
    def get_quickship_label_requested(self):
        return self.quickship_label_requested
    def set_quickship_label_requested(self, quickship_label_requested):
        self.quickship_label_requested = quickship_label_requested
    def get_expected_mailing_date(self):
        return self.expected_mailing_date
    def set_expected_mailing_date(self, expected_mailing_date):
        self.expected_mailing_date = expected_mailing_date
    def get_delivery_spec(self):
        return self.delivery_spec
    def set_delivery_spec(self, delivery_spec):
        self.delivery_spec = delivery_spec
    def get_return_spec(self):
        return self.return_spec
    def set_return_spec(self, return_spec):
        self.return_spec = return_spec
    def get_refund_request_info(self):
        return self.refund_request_info
    def set_refund_request_info(self, refund_request_info):
        self.refund_request_info = refund_request_info
    def _hasContent(self):
        if (
            self.groupIdOrTransmitShipment is not None or
            self.quickship_label_requested is not None or
            self.expected_mailing_date is not None or
            self.delivery_spec is not None or
            self.return_spec is not None or
            self.refund_request_info is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='shipment-detailType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('shipment-detailType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'shipment-detailType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='shipment-detailType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='shipment-detailType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='shipment-detailType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='shipment-detailType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.groupIdOrTransmitShipment is not None:
            self.groupIdOrTransmitShipment.export(outfile, level, namespaceprefix_, namespacedef_='', pretty_print=pretty_print)
        if self.quickship_label_requested is not None:
            namespaceprefix_ = self.quickship_label_requested_nsprefix_ + ':' if (UseCapturedNS_ and self.quickship_label_requested_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%squickship-label-requested>%s</%squickship-label-requested>%s' % (namespaceprefix_ , self.gds_format_boolean(self.quickship_label_requested, input_name='quickship-label-requested'), namespaceprefix_ , eol_))
        if self.expected_mailing_date is not None:
            namespaceprefix_ = self.expected_mailing_date_nsprefix_ + ':' if (UseCapturedNS_ and self.expected_mailing_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexpected-mailing-date>%s</%sexpected-mailing-date>%s' % (namespaceprefix_ , self.gds_format_date(self.expected_mailing_date, input_name='expected-mailing-date'), namespaceprefix_ , eol_))
        if self.delivery_spec is not None:
            namespaceprefix_ = self.delivery_spec_nsprefix_ + ':' if (UseCapturedNS_ and self.delivery_spec_nsprefix_) else ''
            self.delivery_spec.export(outfile, level, namespaceprefix_, namespacedef_='', name_='delivery-spec', pretty_print=pretty_print)
        if self.return_spec is not None:
            namespaceprefix_ = self.return_spec_nsprefix_ + ':' if (UseCapturedNS_ and self.return_spec_nsprefix_) else ''
            self.return_spec.export(outfile, level, namespaceprefix_, namespacedef_='', name_='return-spec', pretty_print=pretty_print)
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
        if nodeName_ == 'groupIdOrTransmitShipment':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_, gds_collector_=gds_collector_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <groupIdOrTransmitShipment> element')
            self.groupIdOrTransmitShipment = obj_
            obj_.original_tagname_ = 'groupIdOrTransmitShipment'
        elif nodeName_ == 'quickship-label-requested':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'quickship_label_requested')
            ival_ = self.gds_validate_boolean(ival_, node, 'quickship_label_requested')
            self.quickship_label_requested = ival_
            self.quickship_label_requested_nsprefix_ = child_.prefix
        elif nodeName_ == 'expected-mailing-date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.expected_mailing_date = dval_
            self.expected_mailing_date_nsprefix_ = child_.prefix
        elif nodeName_ == 'delivery-spec':
            obj_ = delivery_specType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.delivery_spec = obj_
            obj_.original_tagname_ = 'delivery-spec'
        elif nodeName_ == 'return-spec':
            obj_ = ReturnSpecType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.return_spec = obj_
            obj_.original_tagname_ = 'return-spec'
        elif nodeName_ == 'refund-request-info':
            obj_ = ShipmentRefundRequestInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.refund_request_info = obj_
            obj_.original_tagname_ = 'refund-request-info'
# end class shipment_detailType


class delivery_specType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, service_code=None, sender=None, destination=None, recipient=None, options=None, parcel_characteristics=None, notification=None, print_preferences=None, preferences=None, references=None, customs=None, settlement_info=None, gds_collector_=None, **kwargs_):
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
        self.print_preferences = print_preferences
        self.print_preferences_nsprefix_ = None
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
    def get_print_preferences(self):
        return self.print_preferences
    def set_print_preferences(self, print_preferences):
        self.print_preferences = print_preferences
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
            self.print_preferences is not None or
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
        if self.print_preferences is not None:
            namespaceprefix_ = self.print_preferences_nsprefix_ + ':' if (UseCapturedNS_ and self.print_preferences_nsprefix_) else ''
            self.print_preferences.export(outfile, level, namespaceprefix_, namespacedef_='', name_='print-preferences', pretty_print=pretty_print)
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
            obj_ = optionsType8.factory(parent_object_=self)
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
        elif nodeName_ == 'print-preferences':
            obj_ = PrintPreferencesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.print_preferences = obj_
            obj_.original_tagname_ = 'print-preferences'
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


class optionsType8(GeneratedsSuper):
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
                CurrentSubclassModule_, optionsType8)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if optionsType8.subclass:
            return optionsType8.subclass(*args_, **kwargs_)
        else:
            return optionsType8(*args_, **kwargs_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='optionsType8', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('optionsType8')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'optionsType8':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='optionsType8')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='optionsType8', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='optionsType8'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='optionsType8', fromsubclass_=False, pretty_print=True):
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
# end class optionsType8


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


class cc_receipt_detailsType9(GeneratedsSuper):
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
        self.validate_merchant_nameType10(self.merchant_name)
        self.merchant_name_nsprefix_ = None
        self.merchant_url = merchant_url
        self.validate_merchant_urlType11(self.merchant_url)
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
        self.validate_transaction_typeType12(self.transaction_type)
        self.transaction_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, cc_receipt_detailsType9)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if cc_receipt_detailsType9.subclass:
            return cc_receipt_detailsType9.subclass(*args_, **kwargs_)
        else:
            return cc_receipt_detailsType9(*args_, **kwargs_)
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
    def validate_merchant_nameType10(self, value):
        result = True
        # Validate type merchant-nameType10, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchant-nameType10' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_merchant_urlType11(self, value):
        result = True
        # Validate type merchant-urlType11, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchant-urlType11' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_transaction_typeType12(self, value):
        result = True
        # Validate type transaction-typeType12, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on transaction-typeType12' % {"value": value, "lineno": lineno} )
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='cc-receipt-detailsType9', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('cc-receipt-detailsType9')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'cc-receipt-detailsType9':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='cc-receipt-detailsType9')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='cc-receipt-detailsType9', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='cc-receipt-detailsType9'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='cc-receipt-detailsType9', fromsubclass_=False, pretty_print=True):
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
            # validate type merchant-nameType10
            self.validate_merchant_nameType10(self.merchant_name)
        elif nodeName_ == 'merchant-url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchant_url')
            value_ = self.gds_validate_string(value_, node, 'merchant_url')
            self.merchant_url = value_
            self.merchant_url_nsprefix_ = child_.prefix
            # validate type merchant-urlType11
            self.validate_merchant_urlType11(self.merchant_url)
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
            # validate type transaction-typeType12
            self.validate_transaction_typeType12(self.transaction_type)
# end class cc_receipt_detailsType9


class supplier_account_receipt_detailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, merchant_name=None, merchant_url=None, auth_code=None, auth_timestamp=None, supplier_id=None, charge_amount=None, currency=None, transaction_type=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.merchant_name = merchant_name
        self.validate_merchant_nameType13(self.merchant_name)
        self.merchant_name_nsprefix_ = None
        self.merchant_url = merchant_url
        self.validate_merchant_urlType14(self.merchant_url)
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
        self.charge_amount = charge_amount
        self.charge_amount_nsprefix_ = None
        self.currency = currency
        self.currency_nsprefix_ = None
        self.transaction_type = transaction_type
        self.validate_transaction_typeType15(self.transaction_type)
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
    def validate_merchant_nameType13(self, value):
        result = True
        # Validate type merchant-nameType13, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchant-nameType13' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_merchant_urlType14(self, value):
        result = True
        # Validate type merchant-urlType14, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchant-urlType14' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_transaction_typeType15(self, value):
        result = True
        # Validate type transaction-typeType15, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on transaction-typeType15' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.merchant_name is not None or
            self.merchant_url is not None or
            self.auth_code is not None or
            self.auth_timestamp is not None or
            self.supplier_id is not None or
            self.charge_amount is not None or
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
            # validate type merchant-nameType13
            self.validate_merchant_nameType13(self.merchant_name)
        elif nodeName_ == 'merchant-url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchant_url')
            value_ = self.gds_validate_string(value_, node, 'merchant_url')
            self.merchant_url = value_
            self.merchant_url_nsprefix_ = child_.prefix
            # validate type merchant-urlType14
            self.validate_merchant_urlType14(self.merchant_url)
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
            # validate type transaction-typeType15
            self.validate_transaction_typeType15(self.transaction_type)
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
        rootTag = 'ShipmentType'
        rootClass = ShipmentType
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
        rootTag = 'ShipmentType'
        rootClass = ShipmentType
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
        rootTag = 'ShipmentType'
        rootClass = ShipmentType
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
        rootTag = 'ShipmentType'
        rootClass = ShipmentType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from shipment import *\n\n')
        sys.stdout.write('import shipment as model_\n\n')
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
NamespaceToDefMappings_ = {'http://www.canadapost.ca/ws/shipment-v8': [('CostCentreIDType',
                                              './schemas/shipment.xsd',
                                              'ST'),
                                             ('EmailType',
                                              './schemas/shipment.xsd',
                                              'ST'),
                                             ('CompanyNameType',
                                              './schemas/shipment.xsd',
                                              'ST'),
                                             ('ContactNameType',
                                              './schemas/shipment.xsd',
                                              'ST'),
                                             ('GroupIDType',
                                              './schemas/shipment.xsd',
                                              'ST'),
                                             ('TrackingPINType',
                                              './schemas/shipment.xsd',
                                              'ST'),
                                             ('ShipmentIDType',
                                              './schemas/shipment.xsd',
                                              'ST'),
                                             ('ShipmentStatusType',
                                              './schemas/shipment.xsd',
                                              'ST'),
                                             ('CustomerRequestIdType',
                                              './schemas/shipment.xsd',
                                              'ST'),
                                             ('PromoCodeType',
                                              './schemas/shipment.xsd',
                                              'ST'),
                                             ('GroupsType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('GroupType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ShipmentPriceType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ServiceStandardType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('PricedOptionsType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('PricedOptionType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('AdjustmentsType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('AdjustmentType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ShipmentsType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ShipmentInfoType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ShipmentType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('DeliverySpecType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('CustomsType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('SkuType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('SenderType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('DestinationType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('RecipientAddressType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ReturnSpecType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ReturnRecipientType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('DomesticAddressDetailsType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('AddressDetailsType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('DestinationAddressDetailsType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('OptionType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ParcelCharacteristicsType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('NotificationType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('PrintPreferencesType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('PreferencesType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ReferencesType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('SettlementInfoType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('PreAuthorizedPaymentType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ShipmentDetailsType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ShipmentCCReceiptType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ShipmentReceiptType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ShipmentRefundRequestType',
                                              './schemas/shipment.xsd',
                                              'CT'),
                                             ('ShipmentRefundRequestInfoType',
                                              './schemas/shipment.xsd',
                                              'CT')]}

__all__ = [
    "AddressDetailsType",
    "AdjustmentType",
    "AdjustmentsType",
    "CustomsType",
    "DeliverySpecType",
    "DestinationAddressDetailsType",
    "DestinationType",
    "DomesticAddressDetailsType",
    "GroupIDType",
    "GroupType",
    "GroupsType",
    "NotificationType",
    "OptionType",
    "ParcelCharacteristicsType",
    "PreAuthorizedPaymentType",
    "PreferencesType",
    "PricedOptionType",
    "PricedOptionsType",
    "PrintPreferencesType",
    "RecipientAddressType",
    "ReferencesType",
    "ReturnRecipientType",
    "ReturnSpecType",
    "SenderType",
    "ServiceStandardType",
    "SettlementInfoType",
    "ShipmentCCReceiptType",
    "ShipmentDetailsType",
    "ShipmentInfoType",
    "ShipmentPriceType",
    "ShipmentReceiptType",
    "ShipmentRefundRequestInfoType",
    "ShipmentRefundRequestType",
    "ShipmentType",
    "ShipmentsType",
    "SkuType",
    "cc_receipt_detailsType",
    "cc_receipt_detailsType9",
    "delivery_specType",
    "dimensionsType",
    "groupIdOrTransmitShipment",
    "optionsType",
    "optionsType8",
    "shipment_detailType",
    "sku_listType",
    "supplier_account_receipt_detailsType"
]
