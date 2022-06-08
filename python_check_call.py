
from subprocess import check_call, CalledProcessError


try:

                check_call(
                    [
                        "sudo",
                        "apt-get",
                        "install",
                        "-y",
                        self.apt_inst_combo_box.get(),
                    ],
                    stdout=open(os.devnull, "wb"),
                )
                print("Done")
                pop_apt_inst.destroy()
            except CalledProcessError as e:
                print(e.output)
            info_done()