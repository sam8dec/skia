# Copyright 2015 Google Inc.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
# Build ALMOST everything provided by Skia; this should be the default target.
#
# This omits the following targets that many developers won't want to build:
# - debugger: this requires QT to build
#
{
  'variables': {
    'skia_skip_gui%': 0,
  },
  'targets': [
    {
      'target_name': 'most',
      'type': 'none',
      'dependencies': [
        # The minimal set of static libraries for basic Skia functionality.
        'skia_lib.gyp:skia_lib',

        'bench.gyp:*',
        'example.gyp:HelloWorld',
        'SampleApp.gyp:SampleApp',
        'tools.gyp:tools',
        'pathops_unittest.gyp:*',
        'pathops_skpclip.gyp:*',
        'dm.gyp:dm',
        'visualbench.gyp:visualbench',
        'fuzz.gyp:fuzz',
        'kilobench.gyp:kilobench',
        'viewer.gyp:viewer',
      ],
      'conditions': [
        [ 'skia_gpu == 0', {
          'dependencies!': [
            'visualbench.gyp:visualbench',
            'kilobench.gyp:kilobench',
            'viewer.gyp:viewer',
          ]
        }],
        [ 'skia_os != "android" and skia_os != "linux"', {
          'dependencies!': [
            'kilobench.gyp:kilobench',
          ],
        }],
        [ 'skia_gpu == 0 or skia_os == "android"', {
          'dependencies!': [
            'example.gyp:HelloWorld',
          ],
        }],
        ['skia_os == "android" and skia_vulkan == 1', {
          'dependencies': [
            'android_system.gyp:Viewer_APK',
          ],
        }],
        ['skia_os == "ios"', {
          'dependencies!': [
            'example.gyp:HelloWorld',
            'SampleApp.gyp:SampleApp',
            'visualbench.gyp:visualbench',
          ],
          'dependencies': ['iOSShell.gyp:iOSShell' ],
        }],
        ['skia_os == "mac" or skia_os == "linux"', {
          'dependencies': [ 
            'nanomsg.gyp:*' ,
          ],
        }],
        ['skia_os in ["linux", "mac", "win"]', {
          'dependencies': [
            'skiaserve.gyp:skiaserve',
          ],
        }],
        [ 'skia_vulkan == 0 or (skia_os != "win" and skia_os != "android")', {
          'dependencies!': [
            'viewer.gyp:viewer',
          ],
        }],
        [ 'skia_skip_gui',
          {
            'dependencies!': [
              'example.gyp:HelloWorld',
              'SampleApp.gyp:SampleApp',
              'visualbench.gyp:visualbench',
            ]
          }
        ],
      ],
    },
  ],
}
