import rectangle
import surface
def main():
    r = rectangle.Rectangle(10, 10, 10, 10)
    assert((r.x, r.y, r.h, r.w) == (10,10,10,10))
    r = rectangle.Rectangle(-1, 1, 1, 1)
    assert((r.x, r.y, r.h, r.w) == (1,1,1,1))
    r = rectangle.Rectangle(1, -5, 1, 1)
    assert((r.x, r.y, r.h, r.w) == (1,5,1,1))
    r = rectangle.Rectangle(1, 1, -10, 1)
    assert((r.x, r.y, r.h, r.w) == (1,1,10,1))
    r = rectangle.Rectangle(1, 1, 1, -1000)
    assert((r.x, r.y, r.h, r.w) == (1,1,1,1000))
    s = surface.Surface("self.image.png", 10, 10, 10, 10)
    assert((s.rect.x, s.rect.y, s.rect.h, s.rect.w) == (10,10,10,10))
    srect = s.get_rect()
    assert(srect.x,  s.get_rect().y, srect.h,  srect.w) == (10,10,10,10)
    assert s.image
    print("Test Complete!")
main ()