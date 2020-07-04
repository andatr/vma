from conans import ConanFile, tools
import os
import shutil


class VmaConan(ConanFile):
    name = "vma"
    version = "2.3"
    license = "MIT"
    description = "Vulkan memory allocation library from GPUOpen"
    homepage = "https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator"
    topics = ("vma", "vulkan", "memory", "allocator")
    exports_sources = "include/*", "licenses/*"
    no_copy_source = True

    def source(self):
        zip_name = "vma-2.3.0.zip"
        tools.download("https://codeload.github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/zip/v2.3.0", zip_name)
        tools.check_md5(zip_name, "4EBE3957D75931D8945FC77A91EE4445")
        os.mkdir("include")
        os.mkdir("licenses")
        tools.unzip(zip_name)
        shutil.move("VulkanMemoryAllocator-2.3.0/src/vk_mem_alloc.h", "include")
        shutil.move("VulkanMemoryAllocator-2.3.0/LICENSE.txt", "licenses")
        shutil.rmtree("VulkanMemoryAllocator-2.3.0")
        os.unlink(zip_name)

    def package(self):
        self.copy("*")

