# vma
Conan package for [GPU Open Vulkan Memory Allocator](https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator)

# How To Use

1. Add the corresponding remote to conan:

```bash
conan remote add andatr https://api.bintray.com/conan/andatr/yaga
```

2. Add vma reference to `conanfile.txt`/`conanfile.py`:

```
[requires]
vma/2.3@andatr/stable
```

3. Install dependencies for project:

```bash
conan install PROJECT_PATH --build=missing
```

4. Add following lines to CMakeLists.txt

```cmake
set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR} ${CMAKE_MODULE_PATH})
find_package(vma)
```

5. Add #include statement to C++ file

```cpp
#include <vk_mem_alloc.h>
```