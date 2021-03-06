package armory.logicnode;

import iron.object.LampObject;

class SetLightColorNode extends LogicNode {

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function run() {
		var light:LampObject = inputs[1].get();
		var color:iron.math.Vec4 = inputs[2].get();
		
		if (light == null) return;

		light.data.raw.color[0] = color.x;
		light.data.raw.color[1] = color.y;
		light.data.raw.color[2] = color.z;

		super.run();
	}
}
