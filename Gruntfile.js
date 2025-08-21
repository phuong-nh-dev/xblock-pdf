module.exports = function (grunt) {
    require('time-grunt')(grunt);
    require('load-grunt-tasks')(grunt);

    grunt.initConfig({
        eslint: {
            options: {
                configFile: '.eslintrc.js'
            },
            target: [
                'Gruntfile.js',
                'pdf/static/js/**/*.js'
            ]
        },

        jshint: {
            options: {
                jshintrc: true
            },
            all: {
                files: {
                    src: [
                        'Gruntfile.js',
                        'pdf/static/js/**/*.js'
                    ]
                }
            }
        },

        uglify: {
            options: {
                mangle: false,
                compress: {
                    drop_console: true
                }
            },
            build: {
                files: {
                    'pdf/static/js/pdf_view.min.js': ['pdf/static/js/pdf_view.js'],
                    'pdf/static/js/pdf_edit.min.js': ['pdf/static/js/pdf_edit.js']
                }
            }
        },

        watch: {
            js: {
                files: ['pdf/static/js/**/*.js', '!pdf/static/js/**/*.min.js'],
                tasks: ['jshint', 'uglify']
            }
        }
    });

    grunt.registerTask('default', ['test']);
    grunt.registerTask('test', ['jshint:all', 'eslint']);
    grunt.registerTask('build', ['jshint:all', 'eslint', 'uglify']);
    grunt.registerTask('dev', ['build', 'watch']);
};
