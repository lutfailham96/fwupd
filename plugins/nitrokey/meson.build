if get_option('plugin_nitrokey').disable_auto_if(host_machine.system() != 'linux').allowed()
cargs = ['-DG_LOG_DOMAIN="FuPluginNitrokey"']

plugin_quirks += files('nitrokey.quirk')
plugin_builtin_nitrokey = static_library('fu_plugin_nitrokey',
  sources: [
    'fu-nitrokey-device.c',
    'fu-nitrokey-common.c',
    'fu-nitrokey-plugin.c',
  ],
  include_directories: plugin_incdirs,
  link_with: plugin_libs,
  c_args: cargs,
  dependencies: plugin_deps,
)
plugin_builtins += plugin_builtin_nitrokey

if get_option('tests')
  e = executable(
    'nitrokey-self-test',
    sources: [
      'fu-self-test.c',
    ],
    include_directories: plugin_incdirs,
    dependencies: [
      plugin_deps,
      valgrind,
    ],
    link_with: [
      plugin_libs,
      plugin_builtin_nitrokey,
    ],
    install: true,
    install_rpath: libdir_pkg,
    install_dir: installed_test_bindir,
  )
  test('nitrokey-self-test', e)  # added to installed-tests
endif
endif
